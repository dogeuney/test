import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
res = requests.get(url)
res.raise_for_status()

# print(res.text)
#text를 lxml로 파싱해서 정보를 제공받음.
soup = BeautifulSoup(res.text, "lxml")
#title태그 글자를 가지고옴.
print(soup.title.get_text())
print(soup.a.span)
print(soup.a["href"])
print(soup.a.attrs)

