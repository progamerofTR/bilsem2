#kullanıcıya adını ve kaç kere yazılması gerektiğini soracak ve bunu kaç kere istenirse o kadar yazılacak.

dosya = open("ismin.txt", "w", encoding="utf-8")

isim = input("Merhaba, Adın ne? :")
sayi = int(input("İsmin kaç kere yazılsın? :"))

for i in range(sayi):
    dosya.write(str(isim) + "\n")