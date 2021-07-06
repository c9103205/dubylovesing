import requests
from bs4 import BeautifulSoup
import pandas as pd


class Spider:

    def spiderForPttBeauty(self):
        response = requests.get('https://beautyptt.cc/')
        # print(response.text)
        # print(response.status)
        soup = BeautifulSoup(response.text, "lxml")

        # 查詢所有標籤為a ,class,為 lightgallery-trigger
        a = soup.find_all('a',class_="lightgallery-trigger")
        # print(h3)
        print(a)
        result = '';
        for index in a:
            if index.text != "" :
                result = result + str(index.text) +'\n'\
                         + str(index.get('data-href'))+ '\n';
                # print(index.get('data-href')+index.text);

        # print(result)
        return result;

    def __init__(self):
        pass

if __name__ == "__main__":
    s = Spider();
    data =  s.spiderForPttBeauty()
    print(data);