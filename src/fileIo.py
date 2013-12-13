# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="tomy"
__date__ ="$2013-11-21 4:23:26$"
def readTxt():
    f1=open('./text/new.txt')
    print f1.read()
    f1.close()

def createTxt():
    fnew = open('./text/new.txt','r+')
    fnew.seek(0,2)
    fnew.write("aaa")
    fnew.close()
readTxt()
createTxt()
readTxt()