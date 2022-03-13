#Kullanıcıadı ve şifre alınız..kullanıcı adı olarak "admin" şifre olarak
#123456 girilince "sisteme başarıyla giriş yaptınız" yazsın..
#yanlış girildikçe "kullanıcıadı veya şifre hatalı" yazsın
#tekrar kullanıcıadı ve şifre sorsun!

while True:
    kullaniciadi=input("kullanıcı adınız:")
    şifre=input("parolanız:")
    if kullaniciadi=="admin" and şifre=="123456":
        break
    else:
        print("kullanıcıadı veya parola hatalı")
    print("tekrar giriniz")


