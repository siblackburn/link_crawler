from typing Iterable, tuple
import queue

class CrawlerItem():

    def __init__(self, url, depth):
        self.url = url
        self.depth = depth
        #this is just a class to keep url and depth together
        #Using a class rather than a tuple - because in the future I might want to keep track of more than just the depth count on top of the url
        # classes = more flexible than tuple in this case
        # classes are useful when keeping 2 or more bits of information together

class Crawler:

    def __init__(self, initial_url, max_Depth):
        self.initial_url = initial_url
        self.max_depth = max_Depth

    def crawl_method(self) -> Iterable(tuple(str, str)):
        #to do the crawling work
        # to return a list of tuple. Where each tuple is (from, to)
        # Iterable(tuple(str, str)) >> this is explcitly declaring what type I want to return

        result = list()

        processing_queue = queue.Queue()
        processing_queue.put(CrawlerItem(self.initial_url, 1))
        # don't want a depth counter inside of crawl method. It has to remain relative to the item
        while len(processing_queue) > 0:
            item = processing_queue.get()
            url = item.url
            current_depth = item.depth # depth of the item we're currently processing

            if item.depth < self.max_depth: # only collect new links if you haven't reached max depth required

            #process current item. Pop it out of queue
            # Download the page
            # Get new links
                new_links = []
                for link in new_links:
                    result.append(url + link) # create list with from and to urls
                    processing_queue.put(CrawlerItem(link, current_depth +1))

        return result

    # this queue implementation is breadth first search