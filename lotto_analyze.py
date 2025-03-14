import csv
import os
import random
from collections import Counter
import heapq
data_path = os.path.join(os.path.expanduser("~"),"Downloads","data","data.csv")

lotto_nums = []
with open(data_path,newline='',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        for num in row:
            lotto_nums.append(int(num))
lotto_nums.sort()
a=[]
for i in range(0,7):
    b=random.randint(0,len(lotto_nums)-1)
    a.append(lotto_nums[b])
    for num in lotto_nums:
        if num==a:
            lotto_nums.remove(num)
            break
a.sort()
print(a)
print(lotto_nums)