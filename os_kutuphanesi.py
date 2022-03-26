import os
print(os.getcwd()) #dosyanın yolunu verir
print(os.listdir()) #klasörün içindekileri liste tipinde verir.
for i in os.listdir():#listenin elemanlarına tek tek ulaşmak için 
    print(i)