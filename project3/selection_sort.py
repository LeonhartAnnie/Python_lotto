import timeit

unsort = []
with open("number.txt", "r") as f:
    for line in f:
        unsort.extend([
            int(num) for num in line.strip().split(",") if num.strip() != ''
        ])

def SelectionSort(sorted_list):
    n = len(sorted_list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if sorted_list[j] < sorted_list[min_idx]:
                min_idx = j
        if min_idx != i:
            sorted_list[i], sorted_list[min_idx] = sorted_list[min_idx], sorted_list[i]
    return sorted_list        

SelectionSort_time = timeit.timeit(lambda: SelectionSort(unsort), number=1)
print(f"排序時間為:{SelectionSort_time:.2f}秒")
