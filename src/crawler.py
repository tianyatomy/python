# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="tomy"
__date__ ="$2013-11-21 4:23:26$"
import re
import urllib
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'class="BDE_Image" src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'./imgs/%s.jpg' %x)
        x+=1
    return imglist

html = getHtml("http://tieba.baidu.com/p/2726960882")
#print html
print getImg(html)