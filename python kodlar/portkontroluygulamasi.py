## https://github.com/Realradioactive
## realradioactive tarafından yazılmıştır.


import socket
port_liste=[]
banner_liste=[]
dosya=open("ip.txt","r")
ipler=dosya.read()
dosya.close()

print("Bu program RealRadioActive tarafından yazılmıştır.İllegal Kullanımı Yasaktır.")
print("Pentest ve ağ testleri için geliştirilmiştir.")
print("https://github.com/Realradioactive")
print("--------------------------------------------------------")
print("                 REALRADİOACTİVE                        ")
print("                    EAGLE MAP                           ")
print("--------------------------------------------------------")
print("                              / |/ | .-~/               ")
print("                          T\ Y  I  |/  /                ")
print("         /T               | \I  |  I  Y.-~/             ")
print("        I l   /I       T\ |  |  l  |  T  /              ")
print("     T\ |  \ Y l  /T   | \I  l   \ `  l Y               ")
print(" __  | \l   \l  \I l __l  l   \   `  _. |               ")
print(" \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |               ")
print("  \   ~-. -.  `  \  ^._ ^.  -.  /  \   |               ")
print(".--~-._  ~-  `  _  ~-_.-'-.'' ._ /._ .' ./              ")
print(" >--.  ~-.   ._  ~>-'    '\\   7   7   ]                ")
print("^.___~'--._    ~-{  .-~ .  `\ Y . /    |                ")
print("' <__ ~'-.  ~       /_/   \   \I  Y   : |                ")
print("   ^-.__           ~(_/   \   >._:   | l______          ")
print("                   ^--.,___.-~'  /_/   !  `-.~'--l_ /           ")
print("              (_/ .  ~(   /'     '~'--,Y   -=b-. _)     ")
print("               (_/ .  \  :           / l      c'~o \    ")
print("                \ /    `.    .     .^   \_.-~'~--.  )   ")
print("                 (_/ .   `  /     /       !       )/    ")
print("                  / / _.   '.   .':      /        '     ")
print("                  ~(_/ .   /    _  `  .-<_              ")
print("                    /_/. ' .-~' `.  / \  \          ,z=.")
print("                    ~( /   '  :   | K   '-.~-.______//  ")
print("                      '-,.    l   I/ \_    __{--->._(==.")
print("                       //(     \  <    ~'~'     //      ")
print("                      /' /\     \  \     ,v=.  ((       ")
print("                    .^. / /\     '  }__ //===-  `       ")
print("                   / / ' '  '-.,__ {---(==-             ")
print("                 .^ '       :  T  ~'   ll               ")
print("                / .  .  . : | :!        \\              ")
print("               (_/  /   | | j-'          ~^             ")
print("                 ~-<_(_.^-~' ")
print("Bu program İle özel bir ip ve ip listesini ve istenen Port aralığı taranabilir.")
print("--------------------------------------------------------")
print(" [1]-*Özel İp girmek için seçiniz")
print(" [2]-*ip.txt den İp listesini taramak için seçiniz")
print("--------------------------------------------------------")
ayar=int(input("Seçimizi belirtin 1 veya 2 :"))
print("--------------------------------------------------------")
print(" [1]-*bir port aralığını taramak için seçiniz")
print(" [2]-*sabit bir portu taramak için seçiniz")
print("--------------------------------------------------------")
ayar2=int(input("Seçimizi belirtin 1 veya 2 :"))
print("--------------------------------------------------------")
print(" [1]-*Logs.txt ye bulunan ip ve port bilgileri yazılsın")
print(" [2]-*Log dosyası tutulmasın")
print("--------------------------------------------------------")
ayar3=int(input("Seçimizi belirtin 1 veya 2 :"))
if ayar==1:
    if ayar2==1:
        özelport1 = int(input("tarama için port başlangıcı:"))
        özelport2 = int(input("tarama için port bitişi:"))
        özelip = str(input("İp adresini gir:"))
        for ip in özelip.splitlines():
            print("Taranan İp:", ip, "Taranan Port Aralığı:", özelport1, "-", özelport2)
            print("Tarama Başladı...")
            for port in range(özelport1, özelport2):
                try:
                    soket = socket.socket()
                    soket.connect((str(ip), int(port)))
                    banner = soket.recv(1024)
                    banner_liste.append(str(banner))
                    port_liste.append(str(port))
                    soket.close()
                    print("Açık portlar", port)
                    print("Bilgiler", banner)
                    if ayar3==1:
                    #if "SSH" in str(banner):
                        print("Log dosyasına yeni bulunan port eklendi")
                        log = "ip:"+str(ip) + " port:" +str(port)+"\n"
                        dosya = open("logs.txt", "a")
                        dosya.write(log)
                        dosya.close()
                    elif ayar3==2:
                        print("Hatırlatma - Loglar kapalı.")
                except:
                    pass
        print("Açık Portlar Listesi:",port_liste)
        print("Bulunan Veriler Listesi:",banner_liste)
        print("Tarama Tamamlandı.")

    elif ayar2==2:
        özelip = str(input("İp adresini gir:"))
        sabitport = int(input("Portu yazın:"))
        for ip in özelip.splitlines():
            print("Taranan İp:", ip, "Taranan Port ",sabitport)
            print("Tarama Başladı...")
            for port in range(sabitport-1,sabitport+1):
                try:
                    soket = socket.socket()
                    soket.connect((str(ip), int(port)))
                    banner = soket.recv(1024)
                    banner_liste.append(str(banner))
                    port_liste.append(str(port))
                    soket.close()
                    print("Açık portlar:", port)
                    print("Yakalanan Veriler :", banner)
                    if ayar3 == 1:
                        # if "SSH" in str(banner):
                        print("Log dosyasına yeni bulunan port eklendi")
                        log = "ip:" + str(ip) + " port:" + str(port) + "\n"
                        dosya = open("logs.txt", "a")
                        dosya.write(log)
                        dosya.close()
                    elif ayar3 == 2:
                        print("Hatırlatma - Loglar kapalı.")
                except:
                    pass
        print("Açık Portlar Listesi:", port_liste)
        print("Bulunan Veriler Listesi:", banner_liste)
        print("Tarama Tamamlandı.")
elif ayar==2:
    if ayar2==1:
        özelport1 = int(input("tarama için port başlangıcı:"))
        özelport2 = int(input("tarama için port bitişi:"))
        print("Tarama Başladı...")
        for ip in ipler.splitlines():
            print(ip)
            for port in range(özelport1, özelport2):
                try:
                    soket = socket.socket()
                    soket.connect((str(ip), int(port)))
                    banner = soket.recv(1024)
                    banner_liste.append(str(banner))
                    port_liste.append(str(port))
                    soket.close()
                    print("Açık portlar", port)
                    print("Bilgiler", banner)
                    if ayar3 == 1:
                        # if "SSH" in str(banner):
                        print("Log dosyasına yeni bulunan port eklendi")
                        log = "ip:" + str(ip) + " port:" + str(port) + "\n"
                        dosya = open("logs.txt", "a")
                        dosya.write(log)
                        dosya.close()
                    elif ayar3 == 2:
                        print("Hatırlatma - Loglar kapalı.")
                except:
                    pass
        print("Açık Portlar Listesi:", port_liste)
        print("Bulunan Veriler Listesi:", banner_liste)
        print("Tarama Tamamlandı.")
    elif ayar2==2:
        sabitport = int(input("Portu yazın:"))
        print("Tarama Başladı...")
        for ip in ipler.splitlines():
            print(ip)
            for port in range(sabitport-1,sabitport+1):
                try:
                    soket = socket.socket()
                    soket.connect((str(ip), int(port)))
                    banner = soket.recv(1024)
                    banner_liste.append(str(banner))
                    port_liste.append(str(port))
                    soket.close()
                    print("Açık portlar:", port)
                    print("Yakalanan Veriler:", banner)
                    if ayar3 == 1:
                        # if "SSH" in str(banner):
                        print("Log dosyasına yeni bulunan port eklendi")
                        log = "ip:" + str(ip) + " port:" + str(port) + "\n"
                        dosya = open("logs.txt", "a")
                        dosya.write(log)
                        dosya.close()
                    elif ayar3 == 2:
                        print("Hatırlatma - Loglar kapalı.")
                except:
                    pass
        print("Açık Portlar Listesi:", port_liste)
        print("Bulunan Veriler Listesi:", banner_liste)
        print("Tarama Tamamlandı.")
else:
    print("Ayarı yanlış belirttin - özel ayar için 1,listeden taramak için 2 deyiniz. \n Program kapanıyor")