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
        pivotIndex = Partition(arr, start, end)
        QuickSort(arr, start, pivotIndex-1)
        QuickSort(arr, pivotIndex+1, end)
    return arr

def Partition(arr, start, end):
    pivot = arr[start]
    leftPointer = start+1
    rightPointer = end
    done = False
    while not done:
        while leftPointer <= rightPointer and arr[leftPointer] <= pivot:
            leftPointer += 1
        while arr[rightPointer] >= pivot and rightPointer >=leftPointer:
            rightPointer -= 1
        if rightPointer < leftPointer:
            done= True
        else:
            arr[leftPointer],arr[rightPointer] = arr[rightPointer],arr[leftPointer]
    arr[start],arr[rightPointer] = arr[rightPointer],arr[start]
    return rightPointer

# 時間測量
QuickSort_time3 = timeit.timeit(lambda: QuickSort(unsort.copy(), 0, len(unsort) - 1), number=1)
print(f"排序時間為:{QuickSort_time3:.2f}秒")

# 印出結果
#print(QuickSort(unsort.copy(), 0, len(unsort) - 1))
