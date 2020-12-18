"""
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın.
Bunu yaparken try,except bloklarını kullanmayı unutmayın.

"""

liste = ["345","sadas","324a","14","kemal"]

for i in liste:
    try:
        i = int(i)
        print(i)
    except:      #tüm hatalar için
        pass     # pass deyimi bir blokun hiçbir şey yapmadığı anlamına geliyor. Python'ın hata vermemesi için kullanabilirsiniz.