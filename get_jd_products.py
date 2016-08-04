#coding:utf-8
import urllib,time,urllib2
from bs4 import BeautifulSoup
import winsound
from urllib import quote
import httplib,codecs
classlist=["p-name"]
jdurl1='http://list.jd.com/list.html?cat=1319,1527,13288&page='
filepath = r'D:\git\python_learn\jd_洗澡用具.txt'
pagerange = range(1,70)

def get_jd_products_info(jdurl):
    req = urllib2.Request(jdurl)
    req.add_header('Accept','image/webp,image/*,*/*;q=0.8')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4')
    req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
    res = urllib2.urlopen(req)
    return res.read()

def main():

    fout = open(filepath.decode('utf-8'), 'a')
    for x in pagerange:
        jdurl = jdurl1 +str(x)
        print jdurl + '' + filepath
        html = get_jd_products_info(jdurl)
        soup=BeautifulSoup(html)
        for classflag in classlist:
            urlclasses = soup.find_all('div',attrs={"class": classflag})
            print len(urlclasses)
            for urlclass in urlclasses:
                if  urlclass != None:
                    child = urlclass.find('a')
                    fout.write(child.get_text().encode('utf-8').strip())
                    fout.write('\n')
    fout.close()
    winsound.PlaySound("*", winsound.SND_ALIAS)
    winsound.PlaySound("*", winsound.SND_ALIAS)
    winsound.PlaySound("*", winsound.SND_ALIAS)

main()