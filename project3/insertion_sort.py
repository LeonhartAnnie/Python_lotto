import timeit

unsort = []
with open("number.txt", "r") as f:
    for line in f:
        unsort.extend([
            int(num) for num in line.strip().split(",") if num.strip() != ''
        ])

def InsertionSort(data):
    n = len(data)
    for i in range(n-1):
        key = data[i+1]
        j = i
        while j >=0 and key < data[j] :
                data[j+1] = data[j]
                j -= 1
        data[j+1] = key
    return data      

InsertionSort_time = timeit.timeit(lambda: InsertionSort(unsort), number=1)
print(f"排序時間為:{InsertionSort_time:.2f}秒")
