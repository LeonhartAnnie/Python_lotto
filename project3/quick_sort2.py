import timeit

# 讀入資料
unsort = []
with open("number.txt", "r") as f:
    for line in f:
        unsort.extend([
            int(num) for num in line.strip().split(",") if num.strip() != ''
        ])

def QuickSort(arr, start, end):
    if start < end:
        pivotIndex = partition(arr, start, end)
        QuickSort(arr, start, pivotIndex - 1)
        QuickSort(arr, pivotIndex + 1, end)
    return arr

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

# 時間測量
QuickSort_time2 = timeit.timeit(lambda: QuickSort(unsort.copy(), 0, len(unsort) - 1), number=1)
print(f"排序時間為:{QuickSort_time2:.2f}秒")

# 印出結果
#print(QuickSort(unsort.copy(), 0, len(unsort) - 1))
