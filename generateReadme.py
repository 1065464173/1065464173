# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re



def addIntro(f):
	txt = ''' 
- 👋 Hi, I’m @Sxuet , a hard-working female programmer
- 👀 I’m interested in listening to music, skateboarding & anything interesting 
- 🌱 I’m currently learning java 
- 💞️ I’m looking for collaborating on programs which can exercises me
- 🌐 Find me on my personal website：[sxuet.top](https://sxuet.top)
- 📫 How to reach me : sxuet0522@foxmail.com  
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

