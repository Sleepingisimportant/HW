import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#define the path of chrome driver
dirname = os.path.dirname(__file__)
chromnDriverPath = os.path.join(dirname, 'chromedriver')


# establish the object of the driver so that the codes are able to operate using the browser
driver=webdriver.Chrome(chromnDriverPath)
src="https://www.ptt.cc/bbs/movie/index.html"
driver.get(src)


#store the objects of good, mediocre, and bad movies into seperate lists as it is required to list the movies with a specific orders
list_good= []
list_mediocre=[]
list_bad=[]

#crawl 10 pages of the PTT movie board
for x in range(10):
    tags=driver.find_elements(By.CLASS_NAME, "title")
    for tag in tags:
        title=tag.text[1:3]
        if title=="好雷":
            list_good.append(tag.text)
        elif title=="普雷":
            list_mediocre.append(tag.text)
        elif title=="負雷":
            list_bad.append(tag.text)
      
    link=driver.find_element(By.LINK_TEXT,"‹ 上頁")
    link.click()

#save the result with a required order in movie.txt
with open("week-3/movie.txt", "w", encoding="utf-8") as file:
    file.write('\n'.join(list_good)+'\n'+'\n'.join(list_mediocre)+'\n'+'\n'.join(list_bad))


driver.close()