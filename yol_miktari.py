"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol
yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""
yol = float(input("gidilecek yol:"))
yakıt_miktari = float(input("km'de ne kadar yakıyor:"))

ödeme = yol *  yakıt_miktari

print("tutar(TL)",ödeme)
"""
gidilecek yol:100
km'de ne kadar yakıyor:4.5
tutar(TL) 450.0
"""