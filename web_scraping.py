import bs4
import requests
from bs4 import BeautifulSoup

res=requests.get("https://en.wikipedia.org/wiki/Machine_learning").text
# print(res)
# print("object type", type(res))

soup=bs4.BeautifulSoup(res,'html5lib')
# print(soup.prettify())

# print(soup.select(".mw-page-container"))
# for i in soup.select(".mw-page-container"):
    # print(i)
    # print(i.text)

# soup=BeautifulSoup("<b class='boldest'>Extremely boldest</b>","html5lib")
# tag=soup.b
# print(tag.text)

url="https://www.javatpoint.com"
html_content=requests.get(url).text
# print(html_content)

soup=BeautifulSoup(html_content,"html5lib")
# print(soup)
# print(soup.prettify())

print(soup.title)

for link in soup.find_all("a"):
    # print(link)
    # print("text is : {}".format(link.text))
    # print("title is:{}".format(link.get("title")))
    print("title is:{}".format(link.get("href ")))



