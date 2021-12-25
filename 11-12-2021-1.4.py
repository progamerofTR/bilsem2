"""
kullanıcıdan 5 tane isim alarak kullanıcıya sorup a dan z ye veya z den a ya sıralamasını isteyin
"""
liste = []
for i in range(5):
    a = input("Bir isim yazınız: ")
    liste.append(a)
b = input("A dan Z ye mi Z den A ya mı? :").upper()
if b=="A-Z":
    liste.sort()
    print(liste)

else:
    liste.sort(reverse=True)
    print(liste)

