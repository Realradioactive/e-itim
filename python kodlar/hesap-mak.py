islem=input("islemi giriniz 1 toplama 2 çıkarma 3 çarpma 4 bölme")
sayi1=int(input("sayi1:"))
sayi2=int(input("sayı2:"))
if islem=="1":
    sonuc=int(sayi1)+int(sayi2)
    print("sonuc:",str(sonuc))



elif islem=="2":

    sonuc=int(sayi1)-int(sayi2)
    print("sonuc",str(sonuc))
elif islem=="3":
    sonuc=int(sayi1)*int(sayi2)
    print("sonuc",str(sonuc))
elif islem=="4":
    sonuc=int(sayi1)/int(sayi2)
    print("sonuc",str(sonuc))