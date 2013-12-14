#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="tomy"
__date__ ="$2013-12-14 15:20:14$"

if __name__ == "__main__":
    print "Hello World";

class Test:
    first = 123
    second =456
    def f(self):
        return 'test'

milo = Test()
print milo.first
print milo.second
print milo.f()