from bs4 import BeautifulSoup, SoupStrainer
import json
import requests
from urllib.parse import urlparse
import re
import os.path


def link_grabber(pages, depth_required):
    initial_list = []  # holds the unsanitised list, including file extensions and non=links
    url_queue = []  # items that haven't been processed in get
    extension_whitelist = ['.html', '.htm', '']

    homepage = urlparse(pages).netloc
    page_request = requests.get(pages, timeout=5)
    page_response = page_request.text
    data = BeautifulSoup(page_response, "html.parser")
    page_content = data.find('body')

    for lines in page_content.findAll('a', attrs={'href': re.compile("(wikipedia)")}):
        initial_list.append(lines.get('href'))

    for items in initial_list:
        if os.path.splitext(items)[1][1:] in extension_whitelist:
            url_queue.append(items)

    return url_queue


page_link = "https://en.wikipedia.org/wiki/Router_(computing)"
depth_required = 4
iteration_count = 0

output = link_grabber(page_link, depth_required)
print(output)

#
# def processed_urls(urls):
#     processed_items = set()
#     for items in urls:
#         if items not in processed_items:
#             processed_items.add(str(depth_count) + " " + " " + page_link + "-> " + items)
#
#     return processed_items


# process_test = processed_urls(output)
# print(process_test)

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



