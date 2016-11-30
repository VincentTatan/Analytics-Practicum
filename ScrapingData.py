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

url = 'https://www.lazada.sg/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()

soup= bs.BeautifulSoup(source,'lxml')

print(soup)
# print(soup.title.string)
# print(soup.title.text)
# print(soup.p)
# print(soup.find_all('p'))

# for paragraph in soup.find_all('p'):
# 	print(paragraph.text.encode('utf-8'))

# print(soup.get_text().encode('utf-8'))

# for url in soup.find_all('a'):
# 	print(url.get('href'))
# Navigating around website
# nav= soup.nav
# for url in nav.find_all('a'):
# 	print(url.get('href'))

# body = soup.body
# for paragraph in body.find_all('p'):
# 	print(paragraph.text.encode('utf-8'))

# for div in soup.find_all('div',class_='body'):
# 	print(div.text.encode('utf-8'))

# Table
# table = soup.table
# table_rows = table.find_all('tr')
# for tr in table_rows:
# 	td = tr.find_all('td')
# 	row = [i.text.encode('utf-8') for i in td]
# 	print row

# Panda web table parsing
# dfs= pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
# for df in dfs:
# 	print(df)
