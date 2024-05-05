import pandas as pd
import matplotlib.pyplot as plt

# Veri setini oku
data = pd.read_csv('veri_seti.csv')

# Aykırı değerleri tespit etmek için fonksiyon
def detect_outliers(data_column):
    outliers = []# Aykırı değerleri tutmak için boş bir liste oluştur
    q1, q3 = calculate_quartiles(data_column)# Verilen sütunun çeyrekliklerini hesapla
    iqr = q3 - q1 # Çeyreklik aralığını hesapla
    lower_bound = q1 - 1.5 * iqr # Alt sınırı hesapla
    upper_bound = q3 + 1.5 * iqr# Üst sınırı hesapla
    index = 0 
    while index < len(data_column):# Sütunun her elemanı için döngü
        value = data_column[index]# Şu anki elemanı al
        if value < lower_bound or value > upper_bound: # Eğer değer alt veya üst sınırların dışındaysa
            outliers.append(value)# Aykırı değer listesine ekle
        index += 1
    return outliers

# Mode hesaplama fonksiyonu 
def mode_calculation(data):
    frequency_dict = {} # Frekansları tutmak için boş bir sözlük oluştur
    index = 0
    while index < len(data):# Veri listesinin her elemanı için döngü
        value = data[index]# Şu anki elemanı al
        if value in frequency_dict:# Eğer değer sözlükte varsa
            frequency_dict[value] += 1# Frekansını bir artır
        else:
            frequency_dict[value] = 1# Yoksa değeri sözlüğe ekle ve frekansını bir yap
        index += 1
    max_frequency = max(frequency_dict.values())# En yüksek frekansı bul
    modes = [key for key, value in frequency_dict.items() if value == max_frequency]# En yüksek frekansa sahip modları bul
    return modes  

# Kutu grafiği çizimi
def draw_boxplot(data):
    plt.figure(figsize=(8, 6))  # Figure objesi oluştur ve boyutunu belirle
    plt.boxplot(data, vert=False)  # Kutu grafiğini çiz
    plt.xlabel('Değerler')  # X eksenini etiketle
    plt.ylabel('Değişkenler')  # Y eksenini etiketle
    plt.title('Değişkenlerin Kutu Grafiği')  # Grafiğin başlığını belirle
    plt.yticks(range(1, len(data.columns) + 1), data.columns)  # Y ekseninin etiketlerini sütun adlarıyla ayarla
    plt.grid(True)  # Izgara çiz
    plt.show()  # Grafiği göster

# Medyan hesaplama fonksiyonu
def median_calculation(data):
    sorted_data = insertion_sort(data)  # Veriyi inseriton sorta göre sırala
    n = len(sorted_data)  # Veri setinin uzunluğunu al
    index = 0  
    while index < n:  # Sıralanmış veri setinin her elemanı için döngü
        if n % 2 == 0:  # Eğer veri setinin uzunluğu çift ise
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2  # Medyanı hesapla
        else:
            return sorted_data[n//2]  # Medyanı hesapla
        index += 1 

# Aritmetik ortalama hesaplama fonksiyonu 
def mean_calculation(data):
    total = 0  # Toplam değişkenini başlat
    count = 0  # Sayım değişkenini başlat
    index = 0  # İndeks değişkenini başlat
    while index < len(data):  # Veri listesinin her elemanı için döngü
        total += data[index]  # Toplama ekle
        count += 1  # Sayımı bir artır
        index += 1  # İndeksi bir artır
    return total / count  


# Aritmetik ortalama mutlak sapma hesaplama fonksiyonu 
def mean_absolute_deviation_calculation(data, mean):
    total = 0 # Toplam değişkenini başlat
    count = 0 # Sayım değişkenini başlat
    index = 0 # İndeks değişkenini başlat
    while index < len(data): # Veri listesinin her elemanı için döngü
        total += abs(data[index] - mean) # Mutlak sapmayı toplama ekle
        count += 1 # Sayımı bir artır
        index += 1 # İndeksi bir artır
    return total / count

# Varyans hesaplama fonksiyonu
def variance_calculation(data, mean):
    total = 0 # Toplam değişkenini başlat
    count = 0 # Sayım değişkenini başlat
    index = 0 # İndeks değişkenini başlat
    while index < len(data): # Veri listesinin her elemanı için döngü
        total += (data[index] - mean) ** 2 # Karelerin toplamını hesapla
        count += 1 # Sayımı bir artır
        index += 1 # İndeksi bir artır
    return total / count

# Standart sapma hesaplama fonksiyonu 
def standard_deviation_calculation(variance):
    return variance ** 0.5# Varyansın karekökü

# Değişim katsayısı hesaplama fonksiyonu 
def coefficient_of_variation_calculation(standard_deviation, mean):
    return standard_deviation / mean# Standart sapmanın ortalama değere oranı

# Çeyrekler açıklığı hesaplama fonksiyonu (Insertion sort algoritması kullanarak)
def calculate_quartiles(data):
    sorted_data = insertion_sort(data)#Veriyi insertion sort ile sırala
    n = len(sorted_data)# Veri setinin uzunluğunu al
    index = 0
    while index < n:# Sıralanmış veri setinin her elemanı için döngü
        q1_index = int(0.25 * n)# Birinci çeyreklik için indeksi hesapla
        q3_index = int(0.75 * n)# Üçüncü çeyreklik için indeksi hesapla
        q1 = sorted_data[q1_index] if n % 4 != 0 else (sorted_data[q1_index - 1] + sorted_data[q1_index]) / 2
        # Birinci çeyreklik değerini hesapla
        q3 = sorted_data[q3_index] if n % 4 != 0 else (sorted_data[q3_index - 1] + sorted_data[q3_index]) / 2
        # Üçüncü çeyreklik değerini hesapla
        index += 1
    return q1, q3

# Sıralama algoritması - Insertion Sort
def insertion_sort(data):
    sorted_data = data.copy()  # Veri setini değiştirmemek için kopyasını al
    index_i = 1
    while index_i < len(sorted_data):
        key = sorted_data[index_i]
        index_j = index_i - 1
        while index_j >= 0 and key < sorted_data[index_j]:
            sorted_data[index_j + 1] = sorted_data[index_j]
            index_j -= 1
        sorted_data[index_j + 1] = key
        index_i += 1
    return sorted_data

# Merkezi eğilim ve merkezi dağılım ölçümlerini hesapla ve sonuçları dosyaya yaz
with open('sonuc.txt', 'w') as file:
    index = 0
    while index < len(data.columns):
        column = data.columns[index]  # Şu anki sütun adını al
        outliers = detect_outliers(data[column])  # Aykırı değerleri tespit et
        mean = mean_calculation(data[column])  # Aritmetik ortalama hesapla
        median = median_calculation(data[column])  # Medyan hesapla
        mode = mode_calculation(data[column])  # Mod hesapla 

        mean_absolute_deviation = mean_absolute_deviation_calculation(data[column], mean)# Ortalama mutlak sapmayı hesapla  
        variance = variance_calculation(data[column], mean) # Varyansı hesapla
        standard_deviation = standard_deviation_calculation(variance) # Standart sapmayı hesapla  
        coefficient_of_variation = coefficient_of_variation_calculation(standard_deviation, mean) # Değişim katsayısını hesapla  
        q1, q3 = calculate_quartiles(data[column])# Çeyrekler açıklığını hesapla
        quartile_range = q3 - q1# Çeyrekler açıklığını hesapla

        file.write(f"Değişken Adı: {column}\n")
        file.write(f"Aykırı Değerler: {outliers}\n")
        file.write(f"Aritmetik Ortalama: {mean}\n")
        file.write(f"Medyan: {median}\n")
        file.write(f"Tepe Değer: {mode}\n")
        file.write(f"Ortalama Mutlak Sapma: {mean_absolute_deviation}\n")
        file.write(f"Varyans: {variance}\n")
        file.write(f"Standart Sapma: {standard_deviation}\n")
        file.write(f"Değişim Katsayısı: {coefficient_of_variation}\n")
        file.write(f"Çeyrekler Açıklığı: {quartile_range}\n\n")
        
        print(f"Değişken Adı: {column}")
        print(f"Aykırı Değerler: {outliers}")
        print(f"Aritmetik Ortalama: {mean}")
        print(f"Medyan: {median}")
        print(f"Tepe Değer: {mode}")
        print(f"Ortalama Mutlak Sapma: {mean_absolute_deviation}")
        print(f"Varyans: {variance}")
        print(f"Standart Sapma: {standard_deviation}")
        print(f"Değişim Katsayısı: {coefficient_of_variation}")
        print(f"Çeyrekler Açıklığı: {quartile_range}\n")

        index += 1

# Kutu grafiğini çiz
draw_boxplot(data)




