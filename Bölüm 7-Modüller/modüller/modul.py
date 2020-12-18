"""
Modüller
python'ın içerisinde bulunan modüller vardır(Lib dosyası içinde). Dışarıdan'da modüller eklenebilir.
Modül bir çok fonksyon ve yapı barındırarak bizi kod yükünden kurtarır.
"""
import math             # Modülü içeri aktarıyoruz. Artık bu modülün tüm fonksiyonlarını kullanabiliriz.
dir(math)               # Math modülünün içindekileri görmek için dir fonksiyonunu kullanabiliriz.

help(math)              # Fonksiyonların görevlerini görebilmek için help fonksiyonunu kullanabiliriz.

help(math.factorial)    # Örneğin ilk olarak math modülünün içindeki factorial fonksiyonu ne iş yapıyor bakalım.
math.factorial(5)       # 120 sonucunu verecektir.
math.floor(5.4)         # aşağıya yuvarlayacak 5
math.ceil(5.4)          # yukarıya yuvarlayacak 6

#---------------------------------------------------------------------

import math as matematik # Modülü artık matematik ismiyle kullanabiliriz.
matematik.factorial(6)   # örnekteki gibi

#----------------------------------------------------------------------

from math import * # Yıldızın anlamı math modülünün içindeki bütün fonksiyonları almak istediğimizi belirtiyor.
factorial(5)       # böylece fonksyonlara direk ulaşabileceğiz

#----------------------------------------------------------------------

from math import factorial,floor # Sadece 2 tanesini dahil ettik. Hepsini değil belirli fonksyonları dahil etmek istedik.import
floor(5.6)

#-----------------------------------------------------------------------


"""
Kendi Modüllerimizi Yazmak
Bu konuda kendi modüllerimizi nasıl yazacağımızı öğrenmeye çalışacağız. Ancak bu derste Python dosyaları 
oluşturacağımız için kendi bilgisayarımızda konuyu anlatmaya çalışacağım. Uygulayacağımız adımlar şu şekilde;

                1. Herhangi bir tane klasör oluşturuyoruz.
                2. Modülümüz ve deneme Python dosyamız aynı dizinde olması gerektiği için 2 tane Python dosyasını da
                bu klasör altında oluşturuyoruz.
                3. modul1.py ve deneme.py dosyası oluşturuyoruz.
                4. modul1.py dosyasının içine istediğimiz kadar fonksiyonu yazıyoruz.
                5. Son olarak da deneme.py dosyasının içinde bu modul1.py modülünü kullanıyoruz.
Peki yazdığımız bir modülü her yerden kullanmak için ne yapacağız ? Bunun için yazdığımız modul1.py dosyasının
Python35/Lib klasörünün altına atmamız gerekiyor. Böylelikle bu modülü de math modülü gibi her dosyada kullanabiliriz.
"""