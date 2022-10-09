import requests
from bs4 import BeautifulSoup



#Latest page number index will change over time. Manaul adjust is required.
page_num=9500
pages_to_be_crawl=10

list_good= []
list_mediocre=[]
list_bad=[]

#crawl 10 pages of the PTT movie board
for x in range(pages_to_be_crawl):

    url="https://www.ptt.cc/bbs/movie/index"+str(page_num)+".html"

    res = requests.get(url) 

    Soup = BeautifulSoup(res.text,'html.parser') 
    tags=Soup.find_all(class_='title') 
    for tag in tags:
        title=tag.text[2:4]

        
        if title=="好雷":
            list_good.append(tag.text[1:])
        elif title=="普雷":
            list_mediocre.append(tag.text[1:])
        elif title=="負雷":
            list_bad.append(tag.text[1:])
      
    page_num-=1


#save the result with a required order in movie.txt
with open("week-3/movie-BeautifulSoup.txt", "w", encoding="utf-8") as file:
    file.write(''.join(list_good)+''.join(list_mediocre)+''.join(list_bad))


