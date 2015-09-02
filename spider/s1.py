#!/usr/bin/env python
import urllib2  
response = urllib2.urlopen('http://www.sougou.com/')  
html = response.read()  
print html
