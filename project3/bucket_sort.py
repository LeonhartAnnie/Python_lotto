import timeit
import math

# 讀入資料
unsort = []
with open("number.txt", "r") as f:
    for line in f:
        unsort.extend([
            int(num) for num in line.strip().split(",") if num.strip() != ''
        ])

def bucketSort(array):
    maxx = max(array)
    minn = min(array)
    size = 5
 
    buckets = [[] for i in range(math.floor((maxx-minn)/size+1))]

    for i in range(len(array)):
        val = int(array[i])
        buckets[math.floor((val-minn)/size)].append(val)
 
    result = []

    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])

        for j in range(len(buckets[i])):
            result.append(buckets[i][j])

    #去除重複數字
    result = list(set(result))
    result.sort(reverse=True)
                
    return result

# 時間測量
bucketSort_time = timeit.timeit(lambda: bucketSort(unsort.copy()), number=1)
print(f"排序時間為:{bucketSort_time:.2f}秒")

# 印出結果
#print(bucketSort(unsort.copy()))
