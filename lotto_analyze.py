import csv
import os
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
print(lotto_nums)