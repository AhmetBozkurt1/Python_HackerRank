import random

# AYNI LİSTE GELMESİ İÇİN İKİSİ BİRLİKTE ÇALIŞTIRILMALI
random.seed(42)
arr = [random.randint(1, 50) for i in range(10)]
sort_arr = sorted(arr)
max_number = max(sort_arr)

while max_number in sort_arr:
    sort_arr.remove(max_number)
    if max_number not in sort_arr:
        print(max(sort_arr))
        break


