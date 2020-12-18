# Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.

import math
print("Hesap makinesi")

while True  :
    x = float(input("x :"))
    islem = input("islem seçiniz : \n1.faktöriyel\n2.alta yuvarla\n3.üste yuvarla\n4.üst alma")

    if(islem == "1"):
        print(math.factorial(x))
    elif(islem == "2"):
        print(math.floor(x))
    elif(islem == "3"):
        print(math.ceil(x))
    elif(islem == "4"):
        y = int(input("üst değer girin y:"))
        print(math.pow(x,y))
    else:
        print("Çıkış")
        break

