import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td",{"class":"title"})
for cartoon in cartoons:
    print(cartoon.a.get_text())
    
cartoons2 = soup.find_all("div",{"class":"rating_type"})
for cartoon2 in cartoons2:
    print(cartoon2.strong.get_text())

# titles = soup.find_all("td",{"class":"title"})
# for title in enumerate(titles):
#     title_txt = title.find("td",{"class":"title"}).a.get_text()
#     print(title_txt)
# print(titles)
# title = soup.tbody.find_all("tr",{"class":"title"})
# # for title in enumerate(titles):
# # title_txt = titles.find("td",{"class":"title"}).a.get_text()
# print(title)