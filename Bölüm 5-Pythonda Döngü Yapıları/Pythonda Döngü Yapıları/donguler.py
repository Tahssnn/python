"""
For Döngüleri
Pythondaki in operatörü , bir elemanın başka bir
listede,demette veya stringte (karakter dizileri) bulunup bulunmadığını kontrol eder.
"""
# Liste elemanlarını toplama
liste = [1,2,3,4,5,6,7]
toplam = 0
for eleman in liste:
    toplam += eleman
print("Toplam",toplam)

#--------------------------------------------------------------------------------

# Çift elemanları bastırma
liste = [1,2,3,4,5,6,7,8,9]

for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)

#--------------------------------------------------------------------------------

# Her bir karakterleri 3 ile çarpma
s = "Python"

for karakter in s:
    print(karakter * 3)


# demetler üzerinde gezinmek listelerle aynı mantıktır.
demet =  (1,2,3,4,5,6,7)

for eleman in demet:
    print(eleman)

"""
While Döngüleri
"""

# Ekrana 40 defa "Python Öğreniyorum" yazdıralım.
i = 0

while (i < 40):
    print("Python Öğreniyorum")
    i +=1

# range() Fonksiyonu
# range(0,20) # 0'dan 20' a kadar (dahil değil) sayı dizisi oluşturur.
# print(*range(5,20,2)) # 5'ten 20'ye kadar olan sayıları 2 atlayarak oluşturur.

for sayı in range(0,10):
    print(sayı)

# break : ifadesi sadece ve sadece içindeki bulunduğu döngüyü sonlandırır.
i = 0 # break kullanmaya çalışalım.

while (i < 20):
    print(i)
    if (i == 10):
        break # i'nin değeri 10 olunca bu koşul sağlanıyor ve  break ifadesiyle karşılaşıldığı için döngü anında sona eriyor.
    i +=1

"""
continue : Döngü herhangi bir yerde ve herhangi bir zamanda continue 
ifadesiyle karşılaştığı zaman geri kalan işlemlerini
yapmadan direk bloğunun başına döner.
liste = [1,2,3,4,5,6,7,8,9] # continue kullanalım.
"""


for i in liste:
    if (i == 3 or i == 5):
        continue
    print("i:",i)


"""
List Comprehension
Bu konuda listeleri üretmek ve oluşturmak Pythonda çok pratik bir yöntem olan
 "List Comprehension" konusunu öğreneceğiz. Biliyorsunuz Pythonda birçok işimizi
çok kısa kodlar halledebiliyoruz. Ancak kodları daha da kısaltmak ve pratik yöntemler
kullanmak her zaman isteriz. Şimdi örneklerimizle list comprehension'ı anlamaya çalışalım.
"""

liste1 = [1,2,3,4,5]

liste2 = [i*2 for i in liste1] # List Comprehension

print(liste2)

# çıktı [2, 4, 6, 8, 10]