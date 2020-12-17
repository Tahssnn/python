"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""
a = int(input("a sayısı:"))
b = int(input("b sayısı:"))
a,b = b,a

print("a sayısı:",a,"b sayısı:",b)

"""
a sayısı:3
b sayısı:6
a sayısı: 6 b sayısı: 3
"""