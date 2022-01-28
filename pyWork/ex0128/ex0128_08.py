import requests
from bs4 import BeautifulSoup

url = "http://corners.gmarket.co.kr/Bestsellers"
res = requests.get(url)
res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")

# # product_names = soup.find_all("div",{"class":"thumb"})
# # names = product_names.get_text()
# product_names = soup.find_all("a",{"class":"itemname"})
# print(len(product_names))
 

# for product_name in product_names:
#     print(product_name.img.get_text())

# for cartoon in cartoons:
#     print(cartoon.a.get_text())
    
# cartoons2 = soup.find_all("div",{"class":"rating_type"})
# for cartoon2 in cartoons2:
#     print(cartoon2.strong.get_text())