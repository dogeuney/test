from email import headerregistry
from django.urls import clear_script_prefix
import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# total_rank = soup.tbody.find_all("tr")
# for rank in total_rank:
#     rank_num = ""
#     rank_txt = rank.find("div",{"class":"ellipsis rank01"}).span.a.get()
    # print("순위", rank_txt.get_text())


ranks = soup.tbody.find_all("tr")
for i,rank in enumerate(ranks):
    rank_num = rank.find("span",{"class":"rank"}).get_text()
    rank_txt = rank.find("div",{"class":"ellipsis rank01"}).span.a.get_text()
    print("{}위 : {}".format{rank_num,rank_txt})