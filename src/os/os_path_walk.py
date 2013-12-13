# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="tomy"
__date__ ="$2013-11-21 4:23:26$"
import os
def dirList(path):
    filelist = os.listdir(path)
    rs = os.walk(path)
    for path,d,filename in rs:
        print path
        print d
        print filename

dirList('../text')