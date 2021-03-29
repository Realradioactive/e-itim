import random
random_sayi=round(random.random()*100)
print(random_sayi)
girilensayi=int(input("0-100 arası sayı gir:"))
while random_sayi !=girilensayi:
    if girilensayi>random_sayi:
        print("büyük girdin")
    else:
        print("küçük oldu")
    girilensayi=int(input("tekrar dene:"))
print("Oldu ya la")