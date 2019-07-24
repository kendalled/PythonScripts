#pip install requests and re
# github.com/kendalled
import requests
import re

# Filtering Function
def filter_func(x):
    ind = x.find('@')+1
    return not (x[ind:ind+1].isdigit())

# Set URL and fetch HTML
url = 'https://allaboutpins.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
site = requests.get(url, headers=headers).content.decode()

# Regexp match for x@x.com, filter out duplicates and JS packages
possible_emails = re.findall('[\w.]+@[\w.]+', site)
res = list(set(filter(filter_func,possible_emails)))

# Print Output
print(possible_emails)
print('\nSorting...\n')
print('RESULT:')
print(res)
      

### possible regexp: [^\s@<>]+@[^\s@<>]+\.[^\s@<>]+

