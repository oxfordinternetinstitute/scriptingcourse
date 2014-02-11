#!/usr/bin/env python
# encoding: utf-8

# Wikilinks downloader and parser
# The purpose of this script is to take a page in Wikipedia, parse the links within
# and store them in a database. 
# 
# It demonstrates the joint use of:
# BeautifulStoneSoup - an xml parser
# sqlalchemy - an interface to the lightweight sqlite
# regular expressions
# Object-oriented classes
#
# Author: Bernie Hogan
# Version: 1.1
# February 11, 2014

from BeautifulSoup import BeautifulStoneSoup #drop beautifulsoup.py into your directory or pip
from sqlalchemy import * # pip install sqlalchemy
import urllib2,urllib
import re, os
import sys

def getWikiPage(page):
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', "OIItestWikibot/1.0")]
	url = "http://en.wikipedia.org/wiki/Special:Export/%s" % urllib.quote(page)
	return opener.open(url).read()

def getTextFromWikiPage(fullpage):	
	# x = page.decode('utf-8','ignore')
	# x = x.encode('ascii','ignore')

	soup = BeautifulStoneSoup(fullpage)
	print soup.mediawiki.page.revision.id
	return soup.mediawiki.page.text

def getWikiLinks(cookedtext):
	# Here is the regular expression. Note, it is not robust.
	# SIMPLE
	wikileeks = re.compile(r'\[\[.*?]\]')
	# print wikileeks.findall(cookedtext)
	
	# LESS SIMPLE - http links
	# wikileeks = re.compile("http://[\w\./?&=%]*")
	
	return wikileeks.findall(cookedtext)

def getLinksFromPage(wikipage):	
	page = getWikiPage(wikipage)
	text = getTextFromWikiPage(page)
	return getWikiLinks(text)

class newdb:
	def __init__ (self,dbname):
		dbexists = False
		if os.path.exists(os.getcwd() + os.sep + dbname + ".db"):
			dbexists = True
		self.db = create_engine('sqlite:///%s.db' % dbname)

		self.connection = self.db.connect()

		self.metadata = MetaData(self.db)
		
		self.link_table = Table('page', 
							self.metadata,
							Column('ArticleName', String(256)),
							Column('Wikilink', String(256)),
							Column('LinkKey', String(256), unique=True,
							primary_key=True),keep_existing=True,)
		
		if not dbexists:
			self.link_table.create()

	def insertLink(self,articlename,wikilink):
		ins = self.link_table.insert(prefixes=['OR IGNORE']).values(ArticleName=articlename,
			Wikilink=wikilink,LinkKey = articlename + "::" + wikilink)
		self.connection.execute(ins)

	def getLinksFromDB(self,getthisrow):
		sel = select([self.link_table.c.Wikilink,self.link_table.c.ArticleName],
				self.link_table.c.ArticleName == getthisrow)
 		result = self.connection.execute(sel)
		for row in result:
			print row			
			
db = newdb("wikilinks")
page = "Canada"

# Here we are getting the list of links
links = getLinksFromPage(page)
# Now we clean them up. 
# First, get rid of the brackets.
links = [x[2:-2] for x in links]
# Second, get rid of the text after the pipe
links = [x.split("|")[0] for x in links]

for c,i in enumerate(links): 
	db.insertLink(page,i)

db.getLinksFromDB(page)
