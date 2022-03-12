def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi+1):
        sonuc = sonuc*i
    print("Cevap:", sonuc)
sayi = int(input("Sayınızı giriniz: "))
faktoriyel(sayi)