import socket
host="0.0.0.0"
port=5000
soket=socket.socket()
soket.bind((host,port))
soket.listen()
conn , addr = soket.accept()
print("Bağlanti saglandi:",str(conn))
mesaj="Bağlantı sağlandi".encode()
conn.send(mesaj)
while True:
    komut=input("komut:")
    conn.send(komut.encode())
    if komut.lower() == "exit" :
        break
    sonuc=conn.recv(1024).decode()
    print(sonuc)
conn.close()
soket.close()
