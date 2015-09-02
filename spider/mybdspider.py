#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import urllib2
import re

# 贴吧爬虫
class tbSpider:
    def __init__(self,url):
        self.myurl=url
        self.datas=[]
        self.mytool=htmlTool()

    # 抓取数据
    def startSpider(self):
        title,sumpage = self.getInfo()
        self.saveDate(title,sumpage)

    # 保存数据
    def saveDate(self,title,sumpage):
        self.getDate(sumpage)
        f = open(title+".txt",'w+')
        f.writelines(self.datas)
        f.close()
        print u"已保存数据。"

    # 抓取帖子信息
    def getInfo(self):
        mypage = urllib2.urlopen(self.myurl).read().decode('utf-8')
        title = self.titleHunter(mypage)
        sumpage = self.pageCounter(mypage)
        print(u"获取到标题,总页数。")
        return title , sumpage

    # 获取数据
    def getDate(self,sumpage):
        url = self.myurl + "&pn="
        for i in range(1,sumpage + 1):
            mypage = urllib2.urlopen(url + str(i)).read().decode('utf-8')
            msgs = re.findall(r'id="post_content.*?>(.*?)</div>',mypage,re.S)
            for msg in msgs:
                data = self.mytool.replace(msg.encode('utf-8'))
                self.datas.append(data + "\n")

    # 总页数
    def pageCounter(self,mypage):
        match = re.search(r'class="red">(\d+?)</span>',mypage,re.S)
        if match:
            sumpage = int(match.group(1))
        else:
            sumpage = 0
            print(u"找不到任何楼主的消息")
        return sumpage

    # 帖子标题
    def titleHunter(self,mypage):
        match = re.search(r'<h1.*?>(.*?)</h1>',mypage,re.S)
        if match:
            title = match.group(1)
        else:
            print(u"找不到标题")
        return title

# 标记、文本处理工具
class htmlTool:
    #去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    #将多行空行删除
    removeNoneLine = re.compile('\n+')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeNoneLine,"\n",x)
        #strip()将前后多余内容删除
        return x.strip()
# 
bdurl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/')) + "?see_lz=1"

# 生成spider并抓取数据
myspider=tbSpider(bdurl)
myspider.startSpider()
