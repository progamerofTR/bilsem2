#kullanıcıya adını soran ve kaç kere yazdırmak istediğini soran program

isim=input("İsminiz nedir? :")

isim2=int(input("Adınızı kaç kere yazayım? :"))

for i in range(isim2):
    print(isim)
