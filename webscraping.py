import requests
import pandas as pd
from bs4 import BeautifulSoup 

response = requests.get("https://www.flipkart.com/search?q=motorola%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&otracker=nmenu_sub_Electronics_0_Motorola%20razr")

soup = BeautifulSoup(response.content, "html.parser")


prices = soup.find_all('div', class_="Nx9bqj")


price = []
for i in prices[0:10]:
    d = i.get_text()
    price.append(d)


ratings=soup.find_all('img',class_="Rza2QY")
rate = []
for j in ratings[0:10]:
    d = j['src']
    rate.append(d)


df=pd.DataFrame()
df["Price"] = price
df["Image"] = rate


df.to_csv('chandr.csv')


