"""
Mantıksal Değerler (Boolean)
True ve False
"""
a =  True
b = False

bool(0)      # false
bool(1)      # sıfırdan farklı tüm değerler true
"""
Ayrıca Pythonda eğer bir değişkenin değerini sonradan belirlemek 
isterseniz geçici olarak bu değişken None (atanmamış anlamında) değerine eşitleyebilirsiniz.
"""
x = None    # Henüz değer atamadık
x = 4       # Şimdi değer atıyoruz.

"""
Karşılaştırma Operatörleri
==  eşittir
!=  eşit değildir
>
<
>=
<=
"""

"""
Mantıksal Bağlaçlar
    and Operatörü
    or Operatörü
    not operatörü
"""

"""
Koşullu Durumlar
"""

# 18 yaş kontrolü
yaş = int(input("Yaşınızı giriniz:"))

if (yaş < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana giremezsiniz.")
print("Mekana hoşgeldiniz.")

#-------------------------------------------------------------------------------

# 18 yaş kontrolü
yaş = int(input("Yaşınızı giriniz:"))

if (yaş < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana giremezsiniz.")
else:
    # else bloğu -  if koşulu sağlanmazsa çalışacak.
    print("Mekana hoşgeldiniz.")

#-------------------------------------------------------------------------------

işlem =  int(input("İşlem seçiniz:")) # 3 tane işlemimiz olsun.

if işlem == 1:
    print("1. işlem seçildi.")
elif işlem == 2:
    print("2. işlem seçildi.")
elif işlem == 3:
    print("3. işlem seçildi.")
else:
    print("Geçersiz İşlem!")

# koşullu durumlarda if kesiblikle bulunmalıdır .Fakat elif ve else isteğe bağlıdır.