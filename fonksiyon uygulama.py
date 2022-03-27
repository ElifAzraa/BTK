# kullanıcıdan verileri alarak dikdörtgen çevresini fonksiyon yaparak hesaplayınız.

def çevre(kisa,uzun):
    return (kisa+uzun)*2
kisakenar=int(input("kisa kenar:"))
uzunkenar=int(input("uzun kenar:"))
def alan(kisa,uzun):
    return(kisa*uzun)
print("dikdörtgenin çevresi:",çevre(kisakenar,uzunkenar))
print("dikdörtgenin alanı:",alan(kisakenar,uzunkenar))


#alan hesaplama
#def alan(a,b):
    #return a*b
#a=int(input("bir sayı giriniz:"))
#b=int(input("bir sayı giriniz:"))
#print("Dikdörtgenin alanı:", alan(a*b))


