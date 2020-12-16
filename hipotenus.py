"""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""
a = int(input("1. dik kenarı:"))
b = int(input("2. dik kenarı:"))

c = (a ** 2 + b ** 2) ** 0.5
print("hipotenüs:",c)
"""
1. dik kenarı:3
2. dik kenarı:4
hipotenüs: 5.0
"""