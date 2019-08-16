# Scrape Surya Inventory
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse 
import urlsplit
from urllib.parse import urlparse
from collections import deque

 headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

                'Accept-Encoding':'gzip, deflate, br',

                'Accept-Language':'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',

                'Cache-Control':'max-age=0',

                'Connection':'keep-alive',

                'Host':'www.surya.com',

                'Upgrade-Insecure-Requests':'1',

                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'

            }

url = 'https://surya.com'

new_urls = deque([url])

processed_urls = set()

# local urls
local_urls = set()

# external urls
foreign_urls = set()

# broken urls
broken_urls = set()

while(len(new_urls)):
    url = new_urls.popleft()
    processed_urls.add(url)

    print('Processing %s' % url)
    try:
        response = requests.get(url,verify=True, headers = headers )

    except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):
        broken_urls.add(url)
        continue

    parts = urlsplit(url)
    base = '{0.netloc}'.format(parts)
    strip_base = base.replace('www.', '')
    base_url = 