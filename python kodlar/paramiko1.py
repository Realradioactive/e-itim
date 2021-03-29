import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect("192.168.1.15",username="hasan",password="hasan")
stdin, stdout, stdrr=ssh.exec_command("ls")
print(stdout.read)
