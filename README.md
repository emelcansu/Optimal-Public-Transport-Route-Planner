# Optimal Toplu Taşıma Hattı Planlayıcısı

Bu proje, yeni bir toplu taşıma hattı için en uygun mahalleyi belirlemeyi amaçlamaktadır. Üç farklı mahalle, nüfus yoğunluğu, mevcut ulaşım altyapısı, maliyet, çevresel etki ve sosyal fayda gibi kriterlere göre değerlendirilir. Karar verme süreci, Çok Kriterli Karar Analizi (MCDA) ve Softmax algoritması kullanılarak gerçekleştirilir.

## Özellikler
- Kriter Değerlendirmesi: Farklı kriterler normalize edilir ve ağırlıklandırılır.
- Softmax Algoritması: Ağırlıklı puanları olasılıklara dönüştürerek en uygun mahalleyi belirler.
- Ölçeklenebilirlik: Daha fazla mahalle veya kriter eklenerek genişletilebilir.

## Nasıl Çalışır?
1. Veri Hazırlama: Her mahalle için tanımlanan kriterlere göre sentetik veriler hazırlanır.
2. Normalizasyon: Kriter değerleri, aynı ölçekte olmaları için normalize edilir.
3. Ağırlıklandırma: Her kriter, önem derecesine göre bir ağırlık alır.
4. Softmax Hesaplaması: Ağırlıklı puanlar, Softmax fonksiyonu kullanılarak olasılıklara dönüştürülür ve en uygun mahalle belirlenir.

Örnek Çıktı:
![image](https://github.com/user-attachments/assets/aafc7351-6233-4c2a-84d3-c8734abe9bd1)
