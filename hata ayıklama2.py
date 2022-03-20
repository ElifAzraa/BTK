try:
    sayi1=int(input("bir sayı giriniz"))
    sayi2=int(input("bir sayı giriniz"))
    print("sayılarınızın bölümü:",sayi1/sayi2)
except ValueError:# hata mesajını özelleştiriyorum.
    print("Girdiğiniz değer int olmalı!")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez")