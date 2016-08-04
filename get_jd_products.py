#coding:utf-8
import urllib,time,urllib2,os
from bs4 import BeautifulSoup
import winsound
from urllib import quote
import httplib,codecs
classlist=["gl-i-wrap j-sku-item"]
jdurl1='http://list.jd.com/list.html?cat=1319,1527,13288&page='
filepath = r'D:\git\python_learn'

def getallpages(caturl):
    html = get_html(caturl)
    soup = BeautifulSoup(html)
    span = soup.find('span',attrs={"class": 'fp-text'})
    return int(span.find('i').string)

def get_cat_url():
    cat_list=[]
    f_cat = open('D:\git\python_learn\jd_cat.txt','r')
    for line in f_cat:
        cat_list.append(line.strip())
    return cat_list


def get_html(jdurl):
    req = urllib2.Request(jdurl)
    req.add_header('Accept','image/webp,image/*,*/*;q=0.8')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4')
    req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
    res = urllib2.urlopen(req)
    return res.read()

def get_product_info(cat):
    cat_info = cat.split('|')
    fout = open(os.path.join(filepath,cat_info[1].decode('utf-8'))+'.txt', 'a')
    caturl = 'http:'+cat_info[0]
    all_pages = getallpages(caturl) + 1
    print 'pages:'+str(all_pages)
    pagerange=range(1,all_pages)
    for x in pagerange:
        product_url = caturl + '&page=' + str(x)
        print '正在处理分类：'+ cat_info[1]+' url:'+ product_url
        html = get_html(product_url)
        soup=BeautifulSoup(html)
        for classflag in classlist:
            urlclasses = soup.find_all('div',attrs={"class": classflag})
            print '找到商品数：'+ str(len(urlclasses))
            for urlclass in urlclasses:
                if  urlclass != None:
                    child_name_div = urlclass.find('div',attrs={"class": 'p-name'})
                    fout.write(child.get_text().encode('utf-8').strip())
                    fout.write('\n')
    fout.close()

def main():
    cat_list = get_cat_url()
    for cat in cat_list:
        get_product_info(cat)

main()