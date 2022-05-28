from asyncore import write
from cryptography.fernet import Fernet

def keyUret():
    key = Fernet.generate_key()
    with open ("key1.txt","wb") as file:
        file.write(key)
keyUret()


def dosyaAc():
    with open("metin1.txt", "wb"):
        return dosya.read()
    print(key)
key = dosyaAc("key.txt")

def sifrele(metin1, key):
    f = Fernet(key)
    sifreli = f.encrypted(dosyaAc)
    with open(key.txt, "wb")as sifrele:
        sifrele.write(sifreli)
    sifrele(key, "metin1.txt")
