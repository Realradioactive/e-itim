import requests
dosya=open("fuzing.txt","r")
icerik=dosya.read()
dosya.close()
header={"Cookie": "__cfduid=d971d240fb2d9f3bfca31bd182664dbd01599769242"}
for i in icerik.split("\n"):
    print(i)
    url="http://kayagibi.com"+str(i)
    sonuc=requests.get(url=url,headers=header)
    if "200" in str(sonuc.status_code):
        print("Dosya veya dizin var:",i)
    else:
        print("Dosya veya dizin yok",i)

