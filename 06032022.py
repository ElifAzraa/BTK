#kullanıcıdan isim, soyisim, telefon numarası alarak bir lisyete atayınız.
bilgiler=[]#boş liste tanımlar.
İsim=input("isminiz:")
soyisim=input("soyisminiz:")
telefonnumarası=input("telefon numaranız:")
bilgiler.append(İsim)# tırnak koyarsak isim şeklinde çıkar kullanıcıdan istemez.
bilgiler.append(soyisim)
bilgiler.append(telefonnumarası)
print(bilgiler)

