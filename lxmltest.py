#pip install requests and re
# github.com/kendalled
### possible regexp: [^\s@<>]+@[^\s@<>]+\.[^\s@<>]+
###  Backup regexp: '[\w.]+@[\w.]+'

import requests
import re

import pandas as pd

# Negative Email Endings
negatives = ['example.com', 'domain.com', 'address.com', 'xxx.xxx', 'email.com', 'yourdomain.com']

# Reads website column, initializes counter variable
df = pd.read_csv('./Argo.csv')
urls = df['website']
counter = 0


def get_email(url):
    
    # Filtering Function
    def filter_func(x):
        ind = x.find('@')+1
        print('filtering...')
        return not (x[ind:] in negatives)


    # Set Headers 

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    
    # Get HTML, regexp match, filter out bad emails
    try:
        
        site = requests.get(url, verify=True, headers=headers, timeout=(2, 2)).content.decode()
        possible_emails = re.findall('[A-Za-z0-9._%+-]{3,}@[a-z]{3,}\.[a-z]{2,}(?:\.[a-z]{2,})?', site)
        print('Fetched Web Page.\n')
        res = list(set(filter(filter_func,possible_emails)))

      
    except:
        print('Web Page Not Found. Deleting...')
        return []
    
    # TODO: Delete row if no email found
    if(not res):
        print('No Emails Found. Deleting...')
        return []

    # TODO: Append to new csv if found
    else:
        print('Emails:\n')
        print(res)
        
        return res

    return []

    
if __name__ == "__main__":
    for link in urls:
        print(link)
        email = get_email(link)
        if(email):
            counter += len(email)
        
        print('------------------------')
        print(str(counter) + ' Email(s) found so far.')
        print('------------------------')



