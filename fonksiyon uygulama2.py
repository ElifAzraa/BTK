#kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek sonucunda True ya da False
#gönderen fonksiyonun python kodu
#kullanıcıadı:admin,şifre:123456 olmalı.

def kontrol(kullanici,şifre):
    if kullanici=="admin" and şifre=="123456":
        return True
    else:
        return False
kullanici=input("kullanıcı adınız:")
şifre=input("şifreniz:")
print("kontrol kullanici,şifre")
