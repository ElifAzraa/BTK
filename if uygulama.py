"""
kullanıcı yılsonu ortalaması girsin. ortalama 85 üstü ise takdir, 70 üstü teşekkür,
bunların dışında ise hiçbir belge alamadınız desin.
"""
ortalama=int(input("Yılsonu ortalamanız:"))
if ortalama>=85:
    print("Takdir belgesi aldınız")
elif ortalama>=70:
    print("Teşekkür belgesi aldınız")
else:
    print("hiçbir belge alamadınız")