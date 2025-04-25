## Üretim Hattı Planlaması

Bu proje, bir üretim hattında belirli işleri farklı makinelerde yaparken oluşan işlem süresi ve makine geçiş maliyetlerine göre **minimum toplam süreyi** hesaplayan bir Python programıdır. Dinamik programlama (DP) kullanılarak çözülmüştür.

---

## Problem Tanımı

Bir üretim sürecinde:
- `n` adet iş vardır. Bu işler sırayla yapılmalıdır.
- `m` adet makine vardır. Her iş, bu makinelerden herhangi birinde yapılabilir.
- Her işin her makinadaki işlem süresi farklı olabilir.
- İşler arasında makineler değiştirilirse, bir **geçiş maliyeti (switch cost)** ortaya çıkar.

Amaç: **Toplam işlem süresi + geçiş maliyetlerini en aza indirmektir.**

---

## Kullanılan Yöntem

- Dinamik programlama kullanılmıştır.
- `dp[i][j]`, i. işin j. makinada yapılması durumunda oluşabilecek en düşük toplam süreyi temsil eder.
- Zaman karmaşıklığı: **O(n × m²)**
- Uzay karmaşıklığı: **O(n × m)**

---

## Örnek Girdi

process_time = [
  -  [4, 6, 8],  # İş 0 için her makinadaki süre
   - [5, 3, 7],  # İş 1
  -  [6, 8, 4]   # İş 2
]

switch_cost = [
   - [0, 2, 3],  # Makine 0'dan diğerlerine geçiş maliyetleri
   - [2, 0, 1],  # Makine 1'den geçiş
   - [3, 1, 0]   # Makine 2'den geçiş
]

---

 ## Çıktı
 
Minimum toplam süre: 14
