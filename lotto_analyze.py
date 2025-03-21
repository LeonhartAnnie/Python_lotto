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
def pull_nums(lotto_nums):
    a = []
    for i in range(0, 6):
        b = random.randint(0, len(lotto_nums) - 1)
        a.append(lotto_nums[b])
        for num in lotto_nums:
            if num == lotto_nums[b]:
                lotto_nums.remove(num)
                break
    a.sort()
    return a
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
    print(f"選到的6個號碼為: {pull_nums(lotto_nums)}")
    plot(lotto_nums)

if __name__ == "__main__":
    main()


