import requests
from bs4 import BeautifulSoup


list_good = []
list_mediocre = []
list_bad = []


pages_to_be_crawl = 10
url = "https://www.ptt.cc/bbs/movie/index.html"

# crawl 10 pages of the PTT movie board
for x in range(pages_to_be_crawl):

    res = requests.get(url)
    Soup = BeautifulSoup(res.text, 'html.parser')

    tags = Soup.find_all(class_='title')
    for tag in tags:
        title = tag.text[2:4]

        if title == "好雷":
            list_good.append(tag.text[1:])
        elif title == "普雷":
            list_mediocre.append(tag.text[1:])
        elif title == "負雷":
            list_bad.append(tag.text[1:])

    paging = Soup.find(lambda tag:tag.name=="a" and "‹ 上頁" in tag.text)
    url = "https://www.ptt.cc"+paging['href']



# save the result with a required order in movie.txt
with open("week-3/movie-BeautifulSoup.txt", "w", encoding="utf-8") as file:
    file.write(''.join(list_good)+''.join(list_mediocre)+''.join(list_bad))
