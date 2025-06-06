import timeit

unsort = []
with open("number.txt", "r") as f:
    for line in f:
        unsort.extend([
            int(num) for num in line.strip().split(",") if num.strip() != ''
        ])

def bubble_sort(sorted_list):
    n = len(sorted_list)
    while n > 1:
        n-=1
        for i in range(n):        
            if sorted_list[i] > sorted_list[i+1]:  
                sorted_list[i], sorted_list[i+1] = sorted_list[i+1], unsort[i]
    return sorted_list

bubble_sort_time = timeit.timeit(lambda: bubble_sort(unsort), number=1)

print(f"排序時間為:{bubble_sort_time:.2f}秒")