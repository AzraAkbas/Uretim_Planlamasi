import sys

def min_total_time(process_time, switch_cost):
    n = len(process_time)     # iş sayısı
    m = len(process_time[0])  # makine sayısı

    # DP tablosu: dp[i][j] = i. işin j. makinada yapılması durumundaki minimum toplam süre
    dp = [[sys.maxsize] * m for _ in range(n)]

    # İlk iş için sadece işleme süresi
    #Bu tablo n satır ve m sütundan oluştuğu için uzay karmaşıklığı O(n × m)
    for j in range(m):
        dp[0][j] = process_time[0][j]

    # Dinamik programlama
    #Bu üçlü döngü nedeniyle zaman karmaşıklığı O(n × m²) olur
    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                cost = dp[i-1][k] + switch_cost[k][j] + process_time[i][j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    # Son işin en düşük maliyetli hali
    return min(dp[n-1])

# Örnek veri
process_time = [
    [4, 6, 8],  # İş 1
    [5, 3, 7],  # İş 2
    [6, 8, 4]   # İş 3
]

switch_cost = [
    [0, 2, 3],  # makine 1'dan diğerlerine geçiş
    [2, 0, 1],  # makine 2'den
    [3, 1, 0]   # makine 3'den
]

# Hesapla
print("Minimum toplam süre:", min_total_time(process_time, switch_cost))

#