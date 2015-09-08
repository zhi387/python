#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib

#
class myLog:
    def __init__(self,url,username,password):
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
        self.url = url
        self.username = username
        self.password = password
        self.cookiefile = './logcookie.dat'
        self.cookie = cookielib.LWPCookieJar()
        cookprocessor = urllib2.HTTPCookieProcessor(self.cookie)
        opener = urllib2.build_opener(cookprocessor)
        urllib2.install_opener(opener)

    def startLog(self):
        postdata = {
            'username':self.username,
            'password':self.password,
            'type':'1'
            }
        postdata = urllib.urlencode(postdata)
        request = urllib2.Request(url,postdata,self.header)
        reponse = urllib2.urlopen(request).read()
        self.cookie.save(self.cookiefile)
        print(reponse)

# 测试实例
url='http://reg.163.com/logins.jsp?type=1&product=mail163&url=http://entry.mail.163.com/coremail/fcg/ntesdoor2?lightweight%3D1%26verifycookie%3D1%26language%3D-1%26style%3D1'
mylog = myLog(url,'lizhicheng.ok@163.com','pw@1632010')
mylog.startLog()
