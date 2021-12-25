"""
kullanıcıdan negatif bir sayı girmesini isteyin, pozitif sayı girdikçe tekrar negatif bir sayı girmesini isteyin, negatif bir sayı girene kadar olay devam eder
"""
sayi = int(input("negatif bir sayi girin"))
while sayi > 0:
    sayi = int(input("negatif bir sayi girin"))
