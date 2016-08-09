#coding:utf-8
import urllib,time,urllib2,os
from bs4 import BeautifulSoup
import winsound
from urllib import quote
import httplib,codecs
import threading
import time
from Queue import Queue

classlist=["gl-i-wrap j-sku-item"]
filepath = r'C:\git\python_learn'
SHARE_Q = Queue()
_WORKER_THREAD_NUM = 10

def getallpages(caturl):
    html = get_html(caturl)
    soup = BeautifulSoup(html)
    span = soup.find('span',attrs={"class": 'fp-text'})
    return int(span.find('i').string)

def get_cat_url():
    cat_list=[]
    f_cat = open('c:\git\python_learn\jd_cat.txt','r')
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

def get_product_info():
    global SHARE_Q
    while not SHARE_Q.empty():
        cat = SHARE_Q.get()
        cat_info = cat.split('|')
        fout = open(os.path.join(filepath,cat_info[1].replace('/','').decode('utf-8'))+'.txt', 'a')
        caturl = 'http:'+cat_info[0]
        all_pages = getallpages(caturl)
        print 'pages:'+str(all_pages)
        pagerange=range(1,all_pages+1)
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
                        child_name_a = child_name_div.find('a')
                        product_name = child_name_a.get_text().encode('utf-8').strip()
                        child_commit_div = urlclass.find('div', attrs={"class": 'p-commit'})
                        child_commit_a = child_commit_div.find('a')
                        product_commit = child_commit_a.get_text().encode('utf-8').strip()
                        product_info = product_name + '|' + product_commit
                        fout.write(product_info)
                        fout.write('\n')
        fout.close()

class MyThread(threading.Thread) :

    def __init__(self, func) :
        super(MyThread, self).__init__()
        self.func = func

    def run(self) :
        self.func()


def main():
    global SHARE_Q
    threads = []
    cat_list = get_cat_url()
    for cat in cat_list:
        SHARE_Q.put(cat)

    for i in xrange(_WORKER_THREAD_NUM):
        thread = MyThread(get_product_info)
        thread.start()
    #     threads.append(thread)
    # for thread in threads:
    #     thread.join()

if __name__ == '__main__':
    main()