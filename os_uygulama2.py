# uygulama : sadece text uzantılı dosyaları yazdırınız.
import os 
for i in os.listdir():
    if ".txt" in i:
        print(i)
