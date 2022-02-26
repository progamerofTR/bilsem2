#öyle bir fonksiyon yazın ki kullanıcının adını gönderdiğinizde hoşgeldin isim yazsın.

isim=input("İsminizi yazın. :")
print("Hoşgeldin", isim)

#kendisine girilen sayının karesinin karesini hesaplasın.

sayi=int(input("Sayı gir:"))

def hesapla(a):
    print(a*a*a*a)
hesapla(sayi)

#girilen bu sayının çift mi tek mi olduğunu ekrana yazsın.

def tekmi(b):
    if b%2 == 0:
        print("Bu sayı çift bir sayıdır.")
    else:
        print("Bu sayı tek bir sayıdır.")
tekmi(sayi)

