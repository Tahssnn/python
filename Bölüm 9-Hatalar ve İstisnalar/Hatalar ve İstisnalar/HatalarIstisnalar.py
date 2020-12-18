"""
Hatalar ve istisnalar
programda oluşabilecek hataları önceden yakalayarak programımızı ona göre düzenleyebiliriz.
Python'da bir çok hata türü vardır.
NameError
ValueError
SyntaxError
ZeroDivisionError
..

https://docs.python.org/3/library/exceptions.html bu siteden tüm hatalara bakabiliriz.
Tabi ki ezberlememize gerek yok prograrmımızı çalıştırdıkça oluşan hatalarımızı görerek yakalayabiliriz.
"""

"""
try , except blokları
try ,except bloklarının yapısı şu şekildedir;

                try:

                    Hata çıkarabilecek kodlar buraya yazılıyor.
                    Eğer hata çıkarsa program uygun olan except bloğuna girecek.
                    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
                except Hata1:
                    Hata1 oluştuğunda burası çalışacak.
                except Hata2:
                    Hata2 oluştuğunda burası çalışacak.

                    //
                    //
                    //
"""
try:

    a = int("324234dsadsad")  # Burası ValueError hatası veriyor.
    print("Program burada")
except:  # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata oluştu")  # Burası çalışır.

print("Bloklar sona erdi")

#------------------------------------------------------------------------------

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:")) # Hata burada oluşuyor. ValueError'a bloğuna giriyoruz.
    print(a / b)
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")

#------------------------------------------------------------------------------

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b)
except (ValueError,ZeroDivisionError): # aynı satırda hatalarımızı genelleştirebiriz
    print("ZeroDivision veya ValueError hatası")

"""
try,except,finally blokları
Bazen programlarımızda her durumda mutlaka çalışmasını istediğimiz kodlar bulunabilir.
Bunun için biz kendi try,except bloklarına ek olarak bir tane finally bloğu ekleyebiliriz.
finally blokları hata olması veya olmaması durumunda mutlaka çalışacaktır. Yapısı şu şekildedir;

                try:

                    Hata çıkarabilecek kodlar buraya yazılıyor.
                    Eğer hata çıkarsa program uygun olan except bloğuna girecek.
                    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
                except Hata1:
                    Hata1 oluştuğunda burası çalışacak.
                except Hata2:
                    Hata2 oluştuğunda burası çalışacak.

                    //
                    //
                    //
                finally:
                    Mutlaka çalışması gereken kodlar buraya yazılacak.
                    Bu blok her türlü çalışacak.
"""
try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b)     # Hata burada oluşuyor. ZeroDivisionError'a bloğuna giriyoruz.
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
finally:             # Bu kısım her durumda mutlaka çalışır
    print("Her durumda çalışıyorum.")

"""
Hata fırlatmak¶
Bazen kendi yazdığımız fonksiyonlar yanlış kullanılırsa kendi hatalarımızı üretip 
Pythonda bu hataları fırlatabiliriz. Bunun içinde raise anahtar kelimesini kullanacağız. 
Hata fırlatma şu şekilde yapılabilmektedir;

            raise HataAdı(opsiyonel hata mesajı)
            
"""
# Verilen string'i ters çevirmek
def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen doğru bir input girin.")
    else:
        return s[::-1]
"""
alabileceğimiz hata şu forma dönüşür

ValueError                                Traceback (most recent call last)
<ipython-input-23-affc1a0b50fd> in <module>()
----> 1 print(terscevir(12))

<ipython-input-20-8f7e1cd7e827> in terscevir(s)
      2 def terscevir(s):
      3     if (type(s) != str):
----> 4         raise ValueError("Lütfen doğru bir input girin.") 
      5     else:
      6         return s[::-1]

ValueError: Lütfen doğru bir input girin.                           #**********************************************
"""