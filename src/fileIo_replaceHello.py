# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="tomy"
__date__ ="$2013-11-21 4:23:26$"

def replaceTxt():
    rf=open('./text/hello.txt','r+')
    conftent = rf.read()
    rf.seek(0,0)
    rf.write(conftent.replace("hello","hello tomy"))
    rf.close()
replaceTxt()