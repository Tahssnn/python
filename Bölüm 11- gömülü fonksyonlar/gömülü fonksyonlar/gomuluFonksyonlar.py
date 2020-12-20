"""
map( fonksyon , (liste,demet vb.) )
örneğin bir liste içerisindeki değerleri sırasıyla fonksiyona uygular ve değer döner.
fonksiyonumuzda ne kadar bilinmeyen var ise o kadar liste veya demet uygulayabiliriz.
"""
def double(x):
    return x * 2    # örneğin bir fonksyon oluşturduk.

list(map(double,[1,2,3,4,5])) # [2, 4, 6, 8, 10] değerini elde ederiz.

#---------------------------------------------------------------------------------------

list(map(lambda x : x ** 2 , (1,2,3,4,5))) # lamda ile de fonksyon tanımlanabilir [1, 4, 9, 16, 25] değerlerini elde ederiz.

#----------------------------------------------------------------------------------------
liste1 = [2,4,6,8]
liste2 = [10,20,30]
liste3 = [1.2,2.5]
list(map(lambda x , y : x * y , liste1, liste2)) # [20, 80, 180] elde edilir.

list(map(lambda x , y , z : x * y * z , liste1, liste2, liste3)) # [24.0, 200.0]

"""
reduce( foksiyon , (liste veya demet gibi veri tipi) )
fonkiyon ilk önce 1. ve 2. elemana uygulanacak sonra bulunan değer ile 3. elemana uygulanacak böylece tek bir değer bulunacak.
"""
from functools import reduce  # reduce fonksiyonu son sürümlerde functools modülüne taşındı.

reduce(lambda x , y : x + y , (1,2,3,4)) # ((1+2)+3)+4 = 10

#--------------------------------------------------------------------------------------------

reduce(lambda x,y : x * y , [1,2,3,4,5]) #   (((1*2)*3)*4)*5 = 120

#--------------------------------------------------------------------------------------------

def maksimum(x,y):  # reduce ile max fonksiyonu
    if (x > y):
        return x
    else:
        return y

reduce(maksimum, [-2,1,100,35,32])   # 100

"""
filter( fonksiyon , iterasyon yapılacak veri tipi )
fonksiyon sonucu sadece True değer döndürenleri elde etmemizi sağlar.
"""
list(filter(lambda x: x % 2 ==0 , range(10))) #[0, 2, 4, 6, 8]

#----------------------------------------------------------------------------------------------

def asal_mi(x):
    i = 2
    if (x == 1):
        return False # Asal değil
    elif(x == 2):
        return True # Asal sayı
    else:
        while(i < x):
            if (x % i == 0):
                return False # Asal Değil
            i += 1
    return True

list(filter(asal_mi,range(100))) #[0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

"""
zip fonksiyonu
elemanları gruplamaya yarar.
"""

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = ["Python","Php","Java","Javascript","C"]

list(zip(liste1,liste2,liste3)) #[(1, 5, 'Python'), (2, 6, 'Php'), (3, 7, 'Java'), (4, 8, 'Javascript')]

"""
Enumerate Fonksiyonu
elemanları indexlerine göre gruplandıır.
"""
list(enumerate(liste3)) #[(0, 'Python'), (1, 'Php'), (2, 'Java'), (3, 'Javascript'), (4, 'C')]

"""
all() içine aldığı değerlerin hepsi True ise True değer döner.
any() içine aldığı değerlerden bir tanesi bile True ise True değer döner.
"""
all([True,True,True])    # True
any([False,False,True])  # True