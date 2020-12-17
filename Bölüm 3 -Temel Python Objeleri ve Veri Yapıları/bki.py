"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
kilo = float(input("kilo:"))
boy = float(input("boy:"))

bki= kilo / (boy * boy)
print(bki)
"""
kilo:75
boy:1.8
23.148148148148145
"""