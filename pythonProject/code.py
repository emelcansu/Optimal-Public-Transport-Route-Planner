import numpy as np

# Mahalle kriterleri
mahalleler = ["Sherlock Mahallesi", "Walter White Mahallesi", "Pedro Mahallesi"]
nufus_yogunlugu = np.array([5000, 4500, 4000])  # Kişi/km²
ulasim_altyapisi = np.array([3, 2, 1])  # 1-5 arasında değerlendirme
maliyet = np.array([7, 8, 9])  # 1-10 (daha düşük daha iyi)
cevresel_etki = np.array([2, 3, 4])  # 1-5 (daha düşük daha iyi)
sosyal_fayda = np.array([5, 4, 3])  # 1-5 (daha yüksek daha iyi)

# Normalizasyon işlemleri
veriler = np.array([
    nufus_yogunlugu / np.max(nufus_yogunlugu),
    ulasim_altyapisi / np.max(ulasim_altyapisi),
    (10 - maliyet) / np.max(10 - maliyet),
    (5 - cevresel_etki) / np.max(5 - cevresel_etki),  #
    sosyal_fayda / np.max(sosyal_fayda)
])

# Kriter ağırlıkları (örneğin: nüfus yoğunluğu daha önemli olabilir)
agirliklar = np.array([0.3, 0.2, 0.2, 0.15, 0.15])

# Ağırlıklı toplam puanı hesapla
toplam_puan = np.sum(veriler * agirliklar[:, np.newaxis], axis=0)

# Softmax uygula (sayısal stabilite için en büyük değeri çıkar)
toplam_puan -= np.max(toplam_puan)
softmax_puanlar = np.exp(toplam_puan) / np.sum(np.exp(toplam_puan))

# Mahalle puanlarını ekrana yazdırma
print("Mahallelerin Softmax Puanları:")
for mahalle, puan in zip(mahalleler, softmax_puanlar):
    print(f"{mahalle}: {puan:.4f}")

# En uygun mahalleyi seçme
en_uygun_mahalle = mahalleler[np.argmax(softmax_puanlar)]
print(f"\nEn uygun toplu taşıma hattı {en_uygun_mahalle} için planlanmalıdır.")