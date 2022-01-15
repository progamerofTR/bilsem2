#Bir txt dosyasına 1'den 1000'e kadar sayıları yazdırınız.
file=open("sayilar.txt","w",encoding="utf,8")
for i in range(1,1001):
    file.write(str(i)+"\n")
file.close()
