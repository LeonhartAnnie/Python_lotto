import csv
import os
import random
import pandas as pd #python -m pip install pandas
import matplotlib.pyplot as plt
#from collections import defaultdict
#import heapq
data_path = os.path.join(os.path.expanduser("~"),"Downloads","data","data.csv")

lotto_nums = []
with open(data_path,newline='',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        for num in row:
            lotto_nums.append(int(num))
a=[]
for i in range(0,7):
    b=random.randint(0,len(lotto_nums)-1)
    a.append(lotto_nums[b])
    for num in lotto_nums:
        if num==lotto_nums[b]:
            lotto_nums.remove(num)
            break
a.sort()
print(f"選到的7個號碼為: {a}")

""" for from collections import defaultdict

count_dict  = defaultdict(int)
for num in lotto_nums:
    count_dict[num] += 1
print(dict(count_dict))
"""
lotto_number_times = pd.Series(lotto_nums).value_counts()
lotto_number_times = lotto_number_times.sort_index()
for num, count in lotto_number_times.items():
    print(f"{num} 出現次數: {count}次")
plt.barh(lotto_number_times.index, lotto_number_times.values, align='center')
plt.xlabel("times")
plt.ylabel("number")
plt.show()

