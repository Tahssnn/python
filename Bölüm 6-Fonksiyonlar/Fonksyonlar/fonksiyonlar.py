"""
Fonksiyonlar
Fonksiyonların Tanımlanması
Fonksiyon tanımlamanın yapısı şu şekildedir;

        def fonksiyon_adı(parametre1,parametre2..... (opsiyonel)):
            # Fonksiyon bloğu
            Yapılacak işlemler
            # dönüş değeri - Opsiyonel

"""
def selamla():
    print("Selam arkadaşlar...")
    print("Nasılsınız?")

# Toplama fonksiyonu
def toplama(a,b,c):
    print("Toplamları:",a+b+c)
    # kullanma toplama(3,4,5)

# faktoriyelini hesaplayan bir fonksiyon yazalım.
def faktoriyel(sayı):
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        print("Faktoriyel", faktoriyel)
    else:
        while (sayı >= 1):
            faktoriyel *= sayı
            sayı -= 1
        print("Faktoriyel", faktoriyel)

"""
Return ifadesi
return ifadesi fonksiyonun işlemi bittikten sonra çağrıldığı yere değer döndürmesi 
anlamı taşır. Böylelikle, fonksiyonda aldığımız değeri bir değişkende depolayabilir 
ve değeri programın başka yerlerinde kullanabiliriz
"""
def toplama(a,b,c):
    return a+b+c # return'un kullanımı
def ikiyle_çarp(a):
    return a*2
    # kullanımı     toplam = toplama(3,4,5)
    #               print(ikiyle_çarp(toplam))