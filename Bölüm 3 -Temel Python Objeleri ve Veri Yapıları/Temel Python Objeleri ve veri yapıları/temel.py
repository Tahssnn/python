a = 10                   # değişken_ismi = değer
b=20
c= (b + 3) - 2*a         # + - * / dört işlem için kullanılır.

a,b = b,a                # değerleri birbiri ile değiştirir.
print(c,a,b)

print(23 // 5)           # tam sayı bölme operatörüdür sonuç 4
print(23 % 5)            # kalanı bulma operatörüdür sonuç 3
print(2 ** 3)            # üst bulma operatörüdür sonuç 8

"""
Stringler = karakter dizileri 'Tahsin' "Tahsin" '''Tahsin'''
indexler ile ulaşılsa bile  stringler değiştirilemez.
"""
x = "Python öğreniyorum"
x[5]                # 5. index n
x[-2]               # sondan 2. index u
print(x[2:10:3])    # x[baslama : bitis : atlama]
print(len(x))       # boy hesaplar

"""
int() integer'a dönüştürür.
float() float'a dönüştürür.
str() string'e dönüştürür.
"""
# \n bir alt satıra geçer \t bir tab boşluk bırakır.
# type() değerin tipini söyler
print(35,21,99,"java",sep="/")                       # 35/21/99/java
print(*"python")                                     # p y h t o n
print(*"tahsin",sep="**")                            # t**a**h**s**i**n
print("{} ve {} nin toplamı {} dır".format(4,5,4+5)) # 4 ve 5 nin toplamı 9 dır
"""
listeler
listelerde indexlenir ve parçalanırlar.
iç içe liste yapılabilir.Ulaşmak için ise Liste[2][1] şeklinde ulaşılır.
"""
liste1 = []                 # boş liste oluşturma
liste2 = list()             # boş liste oluşturma 2
liste3 = [1,2,3,4,"java"]
liste4 = list("merhaba")
print(liste4)               # ['m', 'e', 'r', 'h', 'a', 'b', 'a']

liste3.append(5)            # listeye 5 elemanını ekler.
liste3.pop()                # listeden eleman çıkarır.
liste3.sort()               # listeyi sıralar.
liste3.sort(reverse=True)   # listeyi tersden sıralar.
"""
demetler turplelar
indexleme ve parçalama vardır.
demetler değiştirilemez.
"""
demet1 = (1,2,3,4,5,"java")
demet1.count(3)         # kaç kez 3 değeri oldduğunu sayar.
demet1.index("java")    # hangi indexte olduğunu söyler.

"""
sözlükler
iç içe sözlükler olabilir.sözlük[2][1] şeklinde ulaşılabilir.
.keys() anahtar kelimelere ulaşılır.
.values() değerlerine ulaşılır.
"""
sözlük1 = {"bir":1,"iki":2,"üc":3}
sözlük2 = {}            # boş sözlük oluşturma
sözlük3 = dict()        # boş sözlük oluşturma 2
sözlük1["iki"]          # 2 değerini verir.
sözlük1["beş"] = 5      # yeni ifadeyi sözlüğe ekler.
sözlük1["bir"] = 100    # günceller değiştirir.


