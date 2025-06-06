import timeit

unsort = []
with open("number.txt", "r") as f:
    for line in f:
        unsort.extend([
            int(num) for num in line.strip().split(",") if num.strip() != ''
        ])

def QuickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    left = []
    right = []
    pivot = arr[0]
    for i in range(1,n):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return QuickSort(left) + [pivot] + QuickSort(right)       

QuickSort_time1 = timeit.timeit(lambda: QuickSort(unsort), number=1)
print(f"排序時間為:{QuickSort_time1:.2f}秒")
