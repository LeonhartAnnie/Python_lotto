import requests
from bs4 import BeautifulSoup
import os
import csv

def get_data_path():
    """定義存取路徑，創建資料夾"""
    desktop = os.path.join(os.path.expanduser('~'), 'Downloads')
    data_dir = os.path.join(desktop, 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print("data directory created")
    data_name = os.path.join(data_dir, 'data.csv')
    return data_name

def get_data():
    """取得網頁原始碼，並進行資料整理"""
    url = "https://www.pilio.idv.tw/ltobig/listbigBIG.asp"
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    article = soup.find_all("span",style = "font-size: 32px; font-weight: bold; color: #000000")

    lotto_nums = []
    for a in article:
        text = a.text.strip().replace('\n','').replace('特別號:','').replace(',','')
        numbers = text.split()
        lotto_nums.append(numbers)
    return lotto_nums

def save_data(lotto_nums,file_path):
    """將資料存成csv檔"""
    with open(file_path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["number 1", "number 2", "number 3", "number 4", "number 5", "number 6", "special number"])
        writer.writerows(lotto_nums)
    print("export successfully")

def main():
    data_path = get_data_path()
    lotto_nums = get_data()
    save_data(lotto_nums,data_path)

if __name__ == '__main__':
    main()

    #-----------------