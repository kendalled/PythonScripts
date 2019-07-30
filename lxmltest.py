# GetScraped V2.5.1
# github.com/kendalled
### possible regexp: [^\s@<>]+@[^\s@<>]+\.[^\s@<>]+
###  Backup regexp: '[\w.]+@[\w.]+'

import requests
import re
import unicodecsv as csv
import pandas as pd



# Negative Email Endings
negatives = ['domain.xxx','sentry.wixpress.com', 'example.com', 'domain.com', 'address.com', 'xxx.xxx', 'email.com', 'yourdomain.com']

# Reads website column, initializes counter variable
df = pd.read_csv('./phoenix.csv')
urls = list(dict.fromkeys(df['website']))
counter = 0
final_list = []
print_list = []

 # Set Headers

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def get_email(url):

    # Filtering Function
    def filter_func(x):
        ind = x.find('@')+1
        print('filtering...')
        return not (x[ind:] in negatives)


    # Get HTML, regexp match, filter out bad emails
    try:

        site = requests.get(url, verify=True, headers=headers, timeout=(2, 2)).content.decode()
        possible_emails = re.findall(r'[A-Za-z0-9._%+-]{3,}@[a-z]{3,}\.[a-z]{2,}(?:\.[a-z]{2,})?', site)
        print('Fetched Web Page.\n')
        res = list(set(filter(filter_func,possible_emails)))


    except:
        print('Web Page Not Found. Deleting...')
        return []


    if(not res):
        print('No Emails Found. Deleting...')
        return []


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
            for mail in [elem.lower() for elem in email]:
                final_list.append(mail)

            counter += len(email)

        if(counter >= 1501):
            break
        print('------------------------')
        print(str(counter) + ' Email(s) found so far.')
        print('------------------------')

    with open('PHX-Emails.csv', 'wb') as csvfile:
        final_list = list(set(final_list))
        for i in final_list:
            print_list.append({'email': i})
        fieldnames = ['email']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for data in print_list:
            writer.writerow(data)

    print('File written!')
