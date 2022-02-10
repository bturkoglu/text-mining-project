
# log için math kütüphanesi lazım.
import math


def sozlukOku(goster=False):
    # Esyalar dosyasını okuyalım.
    with open('Esyalar.txt') as f:
        sozluk =f.read().strip().split(',')
        sozluk = [x.strip() for x in sozluk]

    if goster:
        print('Sözlük:',sozluk)

    return sozluk


def metinOku(sozluk, goster = False):
    # Metin dosyası satır satır okunacak.
    # Okunan her satır içinde: Esyalar'deki kelimeler sayılacak.

    # Eğitim Döküman Sayısı
    D = 0  

    frekans = {}
    with open('metin.txt') as f:
        
        for line in f:
            D += 1
            satiradet = []
            for kelime in sozluk:
                adet = line.count(kelime)
                satiradet.append(adet)

            frekans[D]= tuple(satiradet)

    if goster:
        print()
        print('Frekans:')
        for i in frekans:
            print(i,'\t ==>',frekans[i])

    return D, frekans

def dtfTablosu(sozluk, frekans, goster = False):
    # dtf tablosunu oluşturalım
    dtf = {}
    dtf_list = []

    for i,kelime in enumerate(sozluk):
        adet = 0
        for k,v in frekans.items():
            if v[i] > 0:
                adet += 1

        # Esyalar metinde hiç geçmiyorsa, hata vermesin
        if adet == 0:
            adet = 1
            
        idf = math.log10(D/adet)
        # Noktadan sonra 3 hane yeterli olsun
        idf = int(idf*1000)/1000
        dtf[kelime] = (adet, idf)
        dtf_list.append(idf)

    if goster:
        print()
        print('Dtf:')
        for soz in sozluk:
            print('%-15s ==> %s' % (soz, str(dtf[soz])))

        print()
        print('dtf_list:',dtf_list)

    return dtf, dtf_list


def AgirlikTablosu(D, frekans, dtf_list, goster=False):
    # Ağırlık tablosunu oluşturalım.
    w = {}

    for i in range(D):
        v = frekans[i+1]
        liste = []
        for j in range(len(dtf_list)):
            liste.append(v[j] * dtf_list[j])

        w[i+1] = tuple(liste)

    if goster:
        print()
        print('Ağırlık Tablosu')
        for i in w:
            s = ['%.3f' % x for x in w[i]]
            print(i,' ==> ', s)
            

    return w

   
sozluk = sozlukOku(True)
D, frekans = metinOku(sozluk, True)
dtf, dtf_list = dtfTablosu(sozluk, frekans, True)
w = AgirlikTablosu(D, frekans, dtf_list, True)
