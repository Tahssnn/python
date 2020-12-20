"""
ileri seviye sayılar
"""
bin(4)       # 0b100    2'lik tabana çevirir.

hex(20)      # 0x14   16'lık tabana çevirir.

abs(-4.2)    # 4.2 mutlak değer alır.

round(4.8)   # 5   yuvarlama yapar.
round(4.3)   # 4

max(1,2,3,4,-20,100)       # 100 makimum değeri bulur.
min(1,2,3,4,-20,100)       # -20
sum((-1,1,5,10))           # 15 verilen veri tipini toplar.
pow(2,3)                   # 8 üst alır.

"""
ileri seviye stringler
"""

"tahsin".upper()     # TAHSIN
"TAHSIN".lower()     # tahsin

"adadadadadadadadada".replace("a","s")   # sdsdsdsdsdsdsdsdsds

"python".startswith("p")     # p ile mi başlıyor?  True
"python".endswith("on")      # on ile mi bitiyor True

listeA = "python programlama dili".split(" ") # boşluğa göre hepsini liste yapar.  ['python', 'programlama', 'dili']

"xxxxxxxxxxxxxxxxxxxxTahsinxxxxxxxxxxxx".strip("x")      # Tahsin
"xxxxxxxxxxxxxxxxxxxxTahsinxxxxxxxxxxxx".lstrip("x")     # Tahsinxxxxxxxxxxxx
"xxxxxxxxxxxxxxxxxxxxTahsinxxxxxxxxxxxx".rstrip("x")     # xxxxxxxxxxxxxxxxxxxxTahsin

listeB = ["21","12","2020"]
print(":".join(listeB))     # 21:12:2020

"xxxxxxxxxyzxyzxyz".count("x")          # kaç tane x var ?
"xxxxxxxxxyzxyzxyz".count("x",4)        # 4. indexten sonra kaç tane x var?

"Tahhsin".find("h")           # h değeri kaçıncı indexte?
"Tahhsin".rfind("h")          # sondan gelindiğinde h değeri kaçıncı indexte?

"""
İleri seviye Kümeler (sets)
Kümelerin elemanlarına direk index vb. ile ulaşılamıyor.
"""

x = set()           # boş küme oluşturur.
y = {1,2,3}

listeC = [1,2,3,4,1,2,3,4,12,3,4]
z = set(listeC)   # {1, 2, 3, 4, 12}

x.add("Java")       # kümeye eleman ekler.

küme1 = {1,2,3}
küme2 = {1,2,3}
küme1.difference(küme2)        # küme1 fark küme2
küme1.difference_update(küme2) # aynı işlemi küme1'e günceller.

x.discard("Java")           # elemanı çıkarır.

küme1.intersection(küme2)   # küme1 kesişim küme2
küme1.intersection_update(küme2)

küme1.isdisjoint(küme2)     # ayrık kümeler mi ? True False
küme1.issubset(küme2)       # alt küme mi? True False

küme1.union(küme2)           # küme1 birleşim küme2
küme1.update()

"""
ileri seviye listeler
"""
liste = []
liste.append(6)     # 6 değerini ekler.
liste.extend(6)     # 6 değerini çıkarır.

liste.pop(2)        # 2. indexi çıkar.
liste.index(4)      # 4 elemanı kaçıncı indexte ?

liste.count(1)              # kaç tane 1 değeri var ?
liste.sort()                # listeyi sırala
liste.sort(reverse=True)    # listeyi tersten sıralar







