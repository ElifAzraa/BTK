import random
seviye=input ("Bir seviye seçiniz (kolay/orta/zor):").upper()#(lower.):yazıyı küçüğe çevir.(upper.):yazıyı
#büyüğe çevir.

if seviye=="kolay":
    uret=random.randint(1,10)#1 ile 10 arasında rastgele tamsayı üretir.
    print(uret)
elif seviye=="orta":
    uret=random.randint(1,50)
elif seviye=="zor":
    uret=random.randint(1,100)
else:
    print("lütfen doğru giriş yapınız")
while True:
    tahmin=int(input("tahmininiz:"))
    if tahmin==uret:
        print("tebrikler sayıyı buldunuz")
        break
    elif tahmin<uret:
        print("üzgünüz sayınızıbüyütün!")
    else:
        print("üzgünüm,sayınızı küçültün")