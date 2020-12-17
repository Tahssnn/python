"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c

Deltayı Hesaplama:  b ** 2 -  4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)

"""
a = int(input("a katsayısı :"))
b = int(input("b katsayısı:"))
c = int(input("c katsayısı:"))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)

print(x1,x2)
"""
a katsayısı :1
b katsayısı:2
c katsayısı:1
-1.0 -1.0
"""