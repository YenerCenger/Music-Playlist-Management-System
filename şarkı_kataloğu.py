import sqlite3
import time
import random
class Şarkı():

    def __init__(self,isim,şarkıcı,süre,albüm,prodüksiyon_şirketi,çalan_şarkı):
        self.isim = isim
        self.şarkıcı = şarkıcı
        self.süre = süre
        self.albüm = albüm
        self.prodüksiyon_şirketi = prodüksiyon_şirketi
        self.çalan_şarkı = çalan_şarkı

    def __str__(self):

        return """Şarkının İsmi:{}\nŞarkıcının İsmi:{}\nŞarkının Süresi:{}\nAlbümün Adı:{}\nProdüksiyon Şirketi:{}\nÇalan Şarkı:{}\n
        """.format(self.isim,self.şarkıcı,self.süre,self.albüm,self.prodüksiyon_şirketi,self.çalan_şarkı)

class Playlist():

    def __init__(self):
        self.bağlantı_oluştur()

    def bağlantı_oluştur(self):

        self.bağlantı = sqlite3.connect("playlist.db")

        self.cursor = self.bağlantı.cursor()

        sorgu = "Create Table IF NOT EXISTS şarkılar (isim TEXT,şarkıcı TEXT,süre INT,albüm TEXT,prodüksiyon_şirketi TEXT,çalan_şarkı TEXT)"

        self.cursor.execute(sorgu)

        self.bağlantı.commit()

    def bağlantı_kes(self):
        self.bağlantı.close()

    def şarkıları_göster(self):

        sorgu = "Select * From şarkılar"

        self.cursor.execute(sorgu)

        şarkılar = self.cursor.fetchall()

        if (len(şarkılar) == 0):
            print("Bu playlistde herhangi bir şarkı yok.")

        else:
            for i in şarkılar:
                şarkı = Şarkı(i[0],i[1],i[2],i[3],i[4],i[5])
                print(şarkı)

    def şarkı_sorgula(self,isim):

        sorgu = "Select * From şarkılar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        şarkılar = self.cursor.fetchall()

        if (len(şarkılar) == 0):
            print("Bu playlistde bu şarkı bulunmuyor.")

        else:
            şarkı = Şarkı(şarkılar[0][0],şarkılar[0][1],şarkılar[0][2],şarkılar[0][3],şarkılar[0][4],şarkılar[0][5])

            print(şarkı)

    def şarkı_ekle(self,şarkı):

        sorgu = "Insert into şarkılar Values(?,?,?,?,?,?)"

        self.cursor.execute(sorgu,(şarkı.isim,şarkı.şarkıcı,şarkı.süre,şarkı.albüm,şarkı.prodüksiyon_şirketi,şarkı.çalan_şarkı))

        self.bağlantı.commit()

    def şarkı_sil(self,isim):

        sorgu = "Select * From şarkılar where isim = ?"

        self.cursor.execute(sorgu, (isim,))

        şarkı = self.cursor.fetchall()

        if (len(şarkı) == 0):
            print("Böyle Bir Şarkı Yok.")

        else:
            sorgu = "Delete From şarkılar where isim = ?"
            print("Kitap Siliniyor...")
            time.sleep(1)
            print("Kitap Silindi.")
            self.cursor.execute(sorgu,(isim))
            self.bağlantı.commit()

    def prodüksiyon_şirketi_değiş(self,isim,yeni_şirket):

        sorgu = "Select * From şarkılar where isim = ?"

        self.cursor.execute(sorgu, (isim,))

        şarkı = self.cursor.fetchall()

        if (len(şarkı) == 0):
            print("Böyle Bir Şarkı Yok.")

        else:
            print("Değiştiriliyor...")
            time.sleep(1)
            print("Değiştirildi.")
            sorgu = "Update şarkılar set prodüksiyon_şirketi = ? where isim = ?"

            self.cursor.execute(sorgu, (yeni_şirket,isim))
            self.bağlantı.commit()

    def rastgele_şarkı(self):

        sorgu = "Select * From şarkılar"

        self.cursor.execute(sorgu)

        şarkılar = self.cursor.fetchall()

        if (len(şarkılar) == 0):
            print("Bu playlistde şarkı yok.")
            sorgu = "Update şarkılar set çalan_şarkı = ?"
            self.cursor.execute(sorgu,("Yok.",))

        else:
            şarkı1 = random.choice(şarkılar)

            sorgu = "Update şarkılar set çalan_şarkı = ?"

            self.cursor.execute(sorgu,(şarkı1[0],))
            print("Şuan çalan şarkı:",şarkı1[0])
            self.bağlantı.commit()


    def toplam_süre(self):

        sorgu = "Select * From şarkılar"

        self.cursor.execute(sorgu)

        şarkılar = self.cursor.fetchall()

        toplam_süre = 0

        for i in şarkılar:
            toplam_süre += i[2]

        dakika = toplam_süre//60
        saniye = toplam_süre%60
        print("Bu playlistdeki şarkıların toplam süresi {} dakika {} saniyedir.".format(dakika,saniye))


