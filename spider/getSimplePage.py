#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#    
#    net spider
#    get page 
#    same as  .html  
# 
   
import string, urllib2  
   
#def 
def getPage(url):     
        f = open("getpage.html",'w+')  
        m = urllib2.urlopen(url).read()  
        f.write(m)  
        f.close()  
#
url = raw_input(u'input the url:')
getPage(url) 
