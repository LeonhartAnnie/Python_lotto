import timeit

unsort = []
with open("number.txt", "r") as f:
    for line in f:
        unsort.extend([
            int(num) for num in line.strip().split(",") if num.strip() != ''
        ])

def merge(left, right):# 分割數字為每個列表
    result = []

    while len(left) and len(right):
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result = result+left if len(left) else result+right
    return result

def mergeSort(array):#合併且排序列表數字
    if len(array) < 2:
        return array

    mid = len(array)//2
    leftArray = array[:mid]
    rightArray = array[mid:]

    return merge(mergeSort(leftArray),mergeSort(rightArray))       

mergeSort_time = timeit.timeit(lambda: mergeSort(unsort), number=1)
print(f"排序時間為:{mergeSort_time:.2f}秒")