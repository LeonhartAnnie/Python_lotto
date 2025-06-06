import timeit

unsort = []
with open("number.txt", "r") as f:
    for line in f:
        unsort.extend([
            int(num) for num in line.strip().split(",") if num.strip() != ''
        ])

def ShellSort(sorted_list):
    n = len(sorted_list)
    gap = n // 2 
    while gap > 0: 
        for i in range(gap,n): 
            temp = sorted_list[i] 
            j = i 
            while  j >= gap and sorted_list[j-gap] > temp: 
                sorted_list[j] = sorted_list[j-gap] 
                j = j - gap 
            sorted_list[j] = temp 
        gap = gap // 2
    return sorted_list        

ShellSort_time = timeit.timeit(lambda: ShellSort(unsort), number=1)
print(f"排序時間為:{ShellSort_time:.2f}秒")
