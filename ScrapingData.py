# This will set up dirty and quick lazada data from webscraping

# Set up a mock system and PyQT4 so that the server can make a request for javascript html first before getting the web content (soup) for analysis

import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs 
import urllib

class Client(QWebPage):
	def __init__(self,url):
		self.app=QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self.on_page_load)
		self.mainFrame().load(QUrl(url))
		self.app.exec_()

	def on_page_load(self):
		self.app.quit()

# Getting the soup
url = 'https://www.lazada.sg/'
client_response = Client(url)
source = str(client_response.mainFrame().toHtml().toUtf8())
soup = bs.BeautifulSoup(source, 'lxml')


# Printing it to csv dataset

writer = open('Dataset/attributeshomepage.csv', 'wb')

for h3 in soup.find_all('h3',class_='c-product-item__title'):
	print(h3.text.encode('utf-8'))
	writer.write(h3.text.encode('utf-8'))



f.close()

