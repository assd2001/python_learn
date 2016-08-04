from bs4 import BeautifulSoup

f = open('D:\git\python_learn\cat.html','r')
html = f.read()
soup=BeautifulSoup(html)
urlclasses = soup.find_all('dd')
for urlclass in urlclasses:
    aclasses = urlclass.find_all('a')
    for aclass in aclasses:
        if 'cat' in aclass['href']:
            print aclass['href']+'|'+aclass.string