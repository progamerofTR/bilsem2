# kullanıcı adı : admin şifre : 123456 girilince sisteme başarılı giriş yazsın. Kullanıcı adı veya şifre hatalı bir şekilde girildiğinde ekrana kullanıcı adı veya şifre hatalı yazsın.
# Sisteme giriş yapana kadar kullanıcı adı doğru yazılana kadar tekrar tekrar sorsun.
"""
sonsuz kere soracak
doğru bilince break yapacak
doğru, yanlış if ile sorgulanacak
break sonrası while bitiminden devam edecek
sisteme girildi yazacak
"""


while True:
    kullanici_adi = input("Kullanıcı adınızı yazınız. :").lower()
    sifre = input("şifrenizi yazınız. :")
    if kullanici_adi == "admin" and sifre == "123456":
        print("sisteme giriş başarılı!")

        break
    else:
        print("Kullanıcı adı veya şifre hatalı, tekrar deneyin.")


