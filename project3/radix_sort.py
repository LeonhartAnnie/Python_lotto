import timeit

# 讀入資料
unsort = []
with open("number.txt", "r") as f:
    for line in f:
        unsort.extend([
            int(num) for num in line.strip().split(",") if num.strip() != ''
        ])

def radixSort(arr):
    maxNum = max(arr)
    digits = 1
    while maxNum >= 10**digits:
        digits += 1
    for i in range(digits):
        #產生空桶子
        buckets = [[] for _ in range(10)]
        #依據位數大小分類
        for j in arr:
            radix = int(j/(10**i) % 10)
            buckets[radix].append(j)
        #合併桶子的資料
        x = 0
        for y in range(10):
            for num in buckets[y]:
                arr[x] = num
                x += 1
    return arr

# 時間測量
radixSort_time = timeit.timeit(lambda: radixSort(unsort.copy()), number=1)
print(f"排序時間為:{radixSort_time:.2f}秒")

# 印出結果
#print(radixSort(unsort.copy()))
