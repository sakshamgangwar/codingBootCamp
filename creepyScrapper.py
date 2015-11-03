from creepy import Crawler
from threading import Lock
# crawler using creepy
class WebCrawler(Crawler):
    def __init__(self):
        super(WebCrawler, self).__init__()
        self.process_lock = Lock()

    def process_document(self, doc):
        
        if (doc.status==200):
			self.process_lock.acquire()
			#	In order to get content we can use doc.text 
			print 'GET', doc.status, doc.url
			self.process_lock.release()

c = WebCrawler()
c.crawl('https://en.wikipedia.org/wiki/Amazon.com')