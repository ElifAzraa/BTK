#KARŞILAŞTIRMA OPERATÖRLERİ
"""
< : Küçüktür
> : Büyüktür
<= : Küçük eşit
>= : Büyük eşit
== : Eşittir
!= : Eşit değildir
"""
cinsiyet=input("bir harf giriniz:")

if cinsiyet=="e"or cinsiyet=="E": #or iki şarttan biri doğru ise çalışır.
    print("cinsiyet olarak Erkek girdiniz")
    print("if içerisinden selamlar")
elif cinsiyet=="k"or cinsiyet=="K": #2. veya daha sonraki şartları ekelmek için elif kullanılır.
    print("cinsiyet olarak Kadın girdiniz")
    print("şuanda elif içinden mesaj veriyorum")
else: #şartların dışında herhangi birşey girilirse çalışır.
    print("ben sana e ya da k gir demedim mi")
print("şuanda if dışındasın, if in bitti")