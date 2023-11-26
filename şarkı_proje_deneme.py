from playlist_pogramı.şarkı_kataloğu import *
import time
print("""***********************************

Şarkı Programına Hoşgeldiniz.

İşlemler:

1-Şarkıları Göster

2-Şarkı Sorgula

3-Şarkı Ekle

4-Şarkı Sil

5-Prodüksiyon şirketini Değiştir

6-Rastgele Şarkı Seç

7-Toplam Şarkı Süresini Gör

çıkış içim 'q' ya basın
***********************************
""")

playlist = Playlist()

while True:
    işlem = input("İşlem Seçin:")

    if işlem == "q":
        print("Programdan Çıkılıyor...")
        playlist.bağlantı_kes()
        break

    elif işlem == "1":
        playlist.şarkıları_göster()

    elif işlem == "2":
        şarkı = input("Aradığınız Şarkıyı Girin:")
        playlist.şarkı_sorgula(şarkı)

    elif işlem == "3":
        isim = input("Şarknının Adı:")
        şarkıcı = input("Şarkıcı:")
        süre = int(input("Şarknının süresi (saniye):"))
        albüm = input("Şarknının Albümü:")
        prodüksiyon = input("Prodüksiyon Şirketi:")
        çalan_şarkı = "Yok"

        yeni_şarkı = Şarkı(isim,şarkıcı,süre,albüm,prodüksiyon,çalan_şarkı)
        print("Şarkı Ekleniyor...")
        time.sleep(1)
        playlist.şarkı_ekle(yeni_şarkı)
        print("Şarkı Eklendi.")

    elif işlem == "4":
        isim = input("Silmek İstediğiniz Şarkının adını girin:")
        playlist.şarkı_sil(isim)


    elif işlem == "5":
        isim = input("Prodüksiyon Şirketini değiştireceğiniz şarkının adını girin:")
        yeni_şirket = input("Yeni Prodüksiyon Şirketinin Adını Girin:")

        playlist.prodüksiyon_şirketi_değiş(isim,yeni_şirket)

    elif işlem == "6":
        playlist.rastgele_şarkı()

    elif işlem == "7":
        playlist.toplam_süre()