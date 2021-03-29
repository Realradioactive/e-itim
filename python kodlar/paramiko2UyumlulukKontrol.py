import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect("192.168.1.15",username="hasan",password="hasan")
stdin, stdout, stderr = ssh.exec_command("cat /etc/passwd")
for i in (stdout.read().decode("ascii").split("\n")):
    try:
       if 0 == int((str(i).split(":")[2])):
           print("uid sıfır kullanıcı:",str(i).split(":")[0])
    except:
        pass
