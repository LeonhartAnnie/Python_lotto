import csv
import os
import random
import pandas as pd #python -m pip install pandas
import matplotlib.pyplot as plt

def input_data():
    data_path = os.path.join(os.path.expanduser("~"), "Downloads", "data", "data.csv")

    lotto_nums = []
    with open(data_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            for num in row:
                lotto_nums.append(int(num))
    return lotto_nums
import random

def pull_weighted_unique_nums(lotto_nums, count=2):
    unique_selected = set()  # 存放不重複的選取數字
    while len(unique_selected) < count:
        chosen = random.choices(lotto_nums)[0]  # 根據比重選取數字
        unique_selected.add(chosen)  # 添加到 set 中（確保唯一）

        if len(unique_selected) == len(set(lotto_nums)):  # 若已選完所有不同數字
            break

    return sorted(unique_selected)  # 排序後回傳
def plot(lotto_nums):
    lotto_number_times = pd.Series(lotto_nums).value_counts()
    lotto_number_times = lotto_number_times.sort_index()
    for num, count in lotto_number_times.items():
        print(f"{num} 出現次數: {count}次")
    plt.bar(lotto_number_times.index, lotto_number_times.values, align='center')
    plt.title("lotto number analysis")
    plt.xlabel("number")
    plt.ylabel("times")
    plt.show()
def main():
    lotto_nums = input_data()
    print(f"選到的6個號碼為: {pull_weighted_unique_nums(lotto_nums,6)}")
    plot(lotto_nums)

if __name__ == "__main__":
    main()


