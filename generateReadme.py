# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re



def addIntro(f):
	txt = ''' 
- ๐ Hi, Iโm @Sxuet , a hard-working female programmer
- ๐ Iโm interested in listening to music, skateboarding & anything interesting 
- ๐ฑ Iโm currently learning java 
- ๐๏ธ Iโm looking for collaborating on programs which can exercises me
- ๐ Find me on my personal website๏ผ[sxuet.top](https://sxuet.top)
- ๐ซ How to reach me : sxuet0522@foxmail.com  
''' 
	f.write(txt)

f = open('README.md', 'w+')
addIntro(f)
f.write('<table><tr>\n')
f.write('<td valign="top" width="50%">\n')

addProjectInfo(f)
f.write('\n</td>\n')
f.write('<td valign="top" width="50%">\n')
addBlogInfo(f)
f.write('\n</td>\n')
f.write('</tr></table>\n')
f.close 

