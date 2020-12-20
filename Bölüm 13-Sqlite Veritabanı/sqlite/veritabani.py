"""Sqlite Veritabanı ve Tablo Oluşturma

            Relational Database (İlişkisel Veritabanları) : Tablolardan oluşur. Mysql, Sqlite vs.
            DocumentBased Database (Doküman Veritabanları) : Dokümanlardan oluşur. MongoDb, Azure DocumentDb
                               //
                               //
                               //
Sql sorgulama dilidir. Sql dilini incelemek isterseniz şu siteye bakabilirsiniz : https://www.w3schools.com/SQL/deFault.asp
Sunucusuz veri tabanıdır.
                               """

import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz. # kütüphane.db veri tabanınıda olulşturmuş oluyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.


con.close() # Bağlantıyı koparıyoruz.

"""
Kitaplık Tablosu oluşturma
Veritabanında kitaplık isimli bir tablo oluşturmak için şu 2 sorgudan birini kullanabiliriz.

CREATE TABLE kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT , Sayfa_Sayısı INT) - Bu sorgu kitaplık isimli bir tablo oluşturacak ve bu tablonun özellikleri İsim (TEXT --> String),Yazar(TEXT --> String),Yayınevi (TEXT ---> String), Sayfa_Sayısı(INT --- int) olacak. Ancak bu sorguyu arda arda çalıştırırsak "Tablo Already Exists" hatası alacağız.

CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT , Sayfa_Sayısı INT) - Bu sorgu tablo yoksa oluşturacak, tablo varsa hata vermeyecektir. Kodlarımız şu şekilde;
"""

import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)") # Sorguyu çalıştırıyoruz.
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
tablo_oluştur()
con.close() # Bağlantıyı koparıyoruz.

#Şu anda veritabanımıza bağlandık ve kitaplık isimli bir tablonun oluştuğunu görebiliriz.

#------------------------------------------------------------------------------------------------

"""
Tablolara Veri Ekleme
"""

import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',261)")   # eklemek istediğimiz veri
    con.commit()
deger_ekle()
con.close()


#---------------------------------------------------------------------------------------------


# Peki kullanıcıdan aldığımız değerleri tabloya nasıl ekliyoruz ?

import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
isim = input("İsim:")
yazar = input("Yazar:")
yayınevi = input("Yayınevi:")
sayfa_sayısı =  int(input("Sayfa Sayısı:"))


deger_ekle(isim,yazar,yayınevi,sayfa_sayısı)

con.close()

"""
Tablodaki Verileri Çekme¶
Önceki derslerimizde Tablo oluşturmayı ve Tabloya veri eklemeyi öğrenmiştik. Bu derste de tablodaki verileri nasıl çekeceğimizi öğrenmeye çalışacağız. Tablodan veri çekmek için şu SQL sorgularını kullanacağız.

Select * From kitaplık - Tablodaki tüm bilgileri almamızı sağlar.

Select İsim,Yazar From kitaplık Tablodaki tüm bilgileri sadece İsim ve Yazar özelliklerini almamızı sağlar.

Select * From kitaplık where Yayınevi = 'Everest' Sadece Yayınevi özelliği Everest olanları alır.
"""

#1
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık") # Bütün bilgileri alıyoruz.
    data = cursor.fetchall() # Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
    # con.commit() işlemine gerek yok. Çünkü tabloda herhangi bir güncelleme yapmıyoruz.
verileri_al()
con.close()

#-----------------------------------------------------------------------------------------------

#2
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık") # Sadece İsim ve Yazar özelliklerini alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
verileri_al2()
con.close()

#------------------------------------------------------------------------------------------------------

#3
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,)) # Sadece yayınevi ,Everest olan kitapları alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
verileri_al3("Everest")
con.close()

"""
Tablodaki Verileri Güncelleme ve Silme
Bu derste Sqlite veritabanı ile ilgili son olarak verileri güncellemeyi ve silmeyi öğreneceğiz.

Verileri Güncelleme
Tablodaki verileri güncelleme için şöyle bir sorgu kullanabiliriz.

Update kitaplık set Yayınevi = 'Everest' where Yayınevi = 'Doğan Kitap' -- Yayınevi 'Doğan Kitap' olan kitapların Yayınevi bilgilerini 'Everest' e günceller.
"""

import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,))
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verigüncelle(yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi =  ?",("Everest",yayınevi))
    con.commit()

verigüncelle("Doğan Kitap")
con.close()

"""
Verileri Silme
Tablodaki verileri silme için şöyle bir sorgu kullanabiliriz.

Delete From kitaplık where Yazar = 'Ahmet Ümit' -- Yazar özelliği 'Ahmet Ümit' olan kitapları tablodan siler.
"""

import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()


def deger_ekle(isim, yazar, yayınevi, sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)", (isim, yazar, yayınevi, sayfa_sayısı))
    con.commit()


def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)


def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)


def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?", (yayınevi,))
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)


def verigüncelle(yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi =  ?", ("Everest", yayınevi))
    con.commit()


def verilerisil(yazar):
    cursor.execute("Delete  From kitaplık where Yazar = ?", (yazar,))
    con.commit()


verilerisil("Ahmet Ümit")
con.close()   