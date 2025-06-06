from collections import Counter
import math
import matplotlib.pyplot as plt
import numpy as np

#設定圖表文字為中文
plt.rcParams['font.family'] = 'Microsoft JhengHei'  # or 'DFKai-SB', 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False  # 解決負號亂碼問題

#引入每個排序法時間
print("處理中，請稍後")
from bubble_sort import bubble_sort_time
from bucket_sort import bucketSort_time
from heap_sort import heapSort_time
from insertion_sort import InsertionSort_time
from merge_sort import mergeSort_time
from quick_sort1 import QuickSort_time1
from quick_sort2 import QuickSort_time2
from quick_sort3 import QuickSort_time3
from radix_sort import radixSort_time
from selection_sort import SelectionSort_time
from shell_sort import ShellSort_time
# 每個演算法所花費的時間（秒）
use_time = [bubble_sort_time, bucketSort_time, heapSort_time, InsertionSort_time, mergeSort_time, QuickSort_time1, QuickSort_time2, QuickSort_time3, radixSort_time, SelectionSort_time, ShellSort_time]
# 排序演算法名稱
algorithms_name = ["bubble\nsort\ntime", "bucket\nSort\ntime", "heap\nSort\ntime", "Insertion\nSort\ntime", "merge\nSort\ntime", "Quick\nSort\ntime1", "Quick\nSort\ntime2", "Quick\nSort\ntime3", "radix\nSort\ntime", "Selection\nSort\ntime", "Shell\nSort\ntime"]

print("處理完畢")

unsort = []
with open("number.txt", "r") as f:
    for line in f:
        unsort.extend([
            int(num) for num in line.strip().split(",") if num.strip() != ''
        ])

#將桶排序法弄為副程式，以便後續選擇數字大小使用
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
                
    return result

def first_number():
    begin_number = input("你想查詢的數字開頭為")
    count = sum(1 for x in unsort if str(x).startswith(begin_number))
    print(f"總共有{count}個{begin_number}開頭的數字")

def number_times():
    times_number = input("你想查詢出現數量的數字為")
    count = sum(str(num).count(times_number) for num in unsort)
    print(f"數字{times_number}總共出現{count}次")
    
def number_times_in_list():
    counter = Counter(unsort)
    most_common = counter.most_common(1)[0]  # 取最多的
    print(f"出現最多的數字是 {most_common[0]}，共出現 {most_common[1]} 次")

def max_order():  #use bucket sort
    numbers_for_max = bucketSort(unsort.copy())
    print(len(numbers_for_max))

    while True:
        try:
            maxmin_order = int(input("你想查詢第幾大的數字："))
            if maxmin_order < 1 or maxmin_order > len(numbers_for_max):
                print(f"請輸入 1 到 {len(numbers_for_max)} 之間的整數")
                continue
            sorted_list = sorted(numbers_for_max)
            print(f"第 {maxmin_order} 大的數字為：{sorted_list[maxmin_order - 1]}")
            break
        except ValueError:
            print("請輸入有效的整數")  

def middle():
    numbers_for_middle = bucketSort(unsort.copy())
    print(f"中位數是第{int(1+len(numbers_for_middle)/2)}個數字，數值為:{numbers_for_middle[int(1+len(numbers_for_middle)/2)]}")
    
    
def picture_of_sort_speed():
    import matplotlib.pyplot as plt

    x = list(range(len(use_time)))  # X 軸位置

    plt.bar(x, use_time, color='skyblue')
    plt.title("每個排序法所需要的秒數")
    plt.xlabel("演算法")
    plt.ylabel("時間（秒）")

    # ✅ 1. 設定 X 軸標籤為演算法名稱
    plt.xticks(ticks=x, labels=algorithms_name)

    # ✅ 2. 調整 Y 軸的刻度為 0.5 秒為單位
    max_value = max(use_time)
    plt.yticks([i * 0.5 for i in range(int(max_value / 0.5) + 2)])  # +2 為了保留一點空間

    # ✅ 顯示每個長條的數值
    for i, v in enumerate(use_time):
        plt.text(i, v + 0.01, f"{v:.2f}s", ha='center')

    plt.tight_layout()  # 自動調整排版
    plt.show()


def fast_sort():
    slow_algorithms_time = min(use_time)
    slow_algorithms_name = use_time.index(slow_algorithms_time)

    fast_algorithms_time = max(use_time)
    fast_algorithms_name = use_time.index(fast_algorithms_time)
    print(f"""
    最快的排序法為{fast_algorithms_name}，時間為{fast_algorithms_time:.4}
    最慢的排序法為{slow_algorithms_name}，時間為{slow_algorithms_time:.4}           
    """)
    
def number_distribute():
    # 分組：每10000為一組（例如 1~10000、10001~20000...）
    bins = [i for i in range(0, 100001, 10000)]  # 建立[0, 10000, 20000,...,100000]

    # 使用直方圖計算每一區間有多少筆資料（不畫圖）
    counts, _ = np.histogram(unsort, bins=bins)

    # 建立X軸標籤名稱
    labels = [f"{bins[i]+1}\n~\n{bins[i+1]}" for i in range(len(bins)-1)]
    x = range(len(counts))

    # ✅ 加上每根長條的數值標籤
    for i, count in enumerate(counts):
        plt.text(i, count + max(counts)*0.01, str(count), ha='center', va='bottom', fontsize=9)
    
    #加入 Y 軸上限，避免數值被截斷
    plt.ylim(0, max(counts) * 1.1)  # 上限加 10%，保留空間顯示文字

    # 畫出長條圖
    plt.bar(x, counts, width=0.6, color='skyblue')
    plt.xticks(x, labels,)
    plt.ylabel("數量")
    plt.xlabel("數值區間")
    plt.title("每10000區間共有幾個數字")
    plt.tight_layout()
    plt.show()


def select(function_select):
    while(True):
        try:
            function_select = int(function_select)
            if function_select == 1:
                first_number()
                break
            elif function_select == 2:
                number_times()
                break
            elif function_select == 3:
                number_times_in_list()
                break
            elif function_select == 4:
                max_order()
                break
            elif function_select == 5:
                middle()
                break
            elif function_select == 6:
                picture_of_sort_speed()
                break
            elif function_select == 7:
                fast_sort()
                break
            elif function_select == 8:
                number_distribute()
                break
            elif function_select == 0:
                exit()
            else:
                print("⚠️ 無效的選項，請輸入 1-7")
                break
        except ValueError:
            print("請輸入1~7的數字")
            break

while(True):
    function_select = input("""
    請輸入你想要使用的功能
    1. 查詢有幾個數字開頭為N
    2. 查詢數字N出現的次數
    3. 出現次數最多的數字
    4. 第N大的數字
    5. 中位數
    6. 每個排序的執行時間
    7. 排序速度最快的演算法
    8. 數字區間分布(1000為單位)
    ----------點選0結束程式----------""")
    select(function_select) 
    input("...按下enter繼續執行程式...")
