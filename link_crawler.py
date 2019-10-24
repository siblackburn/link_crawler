from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import re
import os.path
from queue import Queue

class CrawlerItem():

    def __init__(self, url, depth):
        self.url = url
        self.depth = depth
        #this is just a class to keep url and depth together
        #Using a class rather than a tuple - because in the future I might want to keep track of more than just the depth count on top of the url
        # classes = more flexible than tuple in this case
        # classes are useful when keeping 2 or more bits of information together


class Crawler:

    def __init__(self, initial_url, max_depth):
        self.initial_url = initial_url
        self.max_depth = max_depth

    def link_grabber(self):
        results = list()

        processing_queue = Queue()
        processing_queue.put(CrawlerItem(self.initial_url, 1))
        # don't want a depth counter inside of crawl method. It has to remain relative to the item
        while not processing_queue.empty():
            item = processing_queue.get() # returns and also removes an item from the queue
            url = item.url
            current_depth = item.depth # depth of the item we're currently processing

            if item.depth <= self.max_depth: # only collect new links if you haven't reached max depth required

                '''Code to process a link and retrieve links from it'''
                extension_whitelist = ['.html', '.htm', '']

                scheme = urlparse(url).scheme
                homepage = urlparse(url).netloc
                page_request = requests.get(url, timeout=5)
                page_response = page_request.text
                data = BeautifulSoup(page_response, "html.parser")
                page_content = data.find('body')

                processing_list = []
                for lines in page_content.findAll('a', attrs={'href': re.compile("(^/wiki/)")}, limit=10):
                    processing_list.append(scheme + "://" + homepage + lines.get('href'))
                for items in processing_list:
                    if os.path.splitext(items)[1][1:] in extension_whitelist:
                        tup = (url,items)
                        results.append(tup)
                        processing_queue.put(CrawlerItem(items, current_depth + 1))

        return results










'''
Code to test whether the website is working. But it's taking too long to get a response
for urls in url_queue:
    request_test = requests.get(urls)
    if request_test.status_code >= 299:
        url_queue.remove(urls)
    else:
        continue
print(url_queue)
'''



