veri="egitim 101"
egitim=list(veri)
print(egitim)
harf_sayaci=0
rakam_sayici=0
for i in egitim:
    if str(i).isdecimal():
        rakam_sayici+=1
    else:
        harf_sayaci+=1
print("rakam sayisi:",rakam_sayici)
print("karakter sayisi:",harf_sayaci)
