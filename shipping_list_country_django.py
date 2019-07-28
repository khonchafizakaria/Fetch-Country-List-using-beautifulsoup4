import urllib3
import json
import time
from bs4 import BeautifulSoup as bs

url = 'https://www.nationsonline.org/oneworld/country_code_list.htm'

# URL Endpoints
view = '<django_view_url>'


http = urllib3.PoolManager()

rs = http.request('GET', url)
soup = bs(rs.data, features='html5lib')

for i in soup.find_all('tr'):
    tds = i.find_all('td')
    list = [j.text.strip() for j in tds if j is not None]
    del list[0]
    try:
        if list[1] == 'UK' or list[1] == 'US' or list[1] == 'CA' or list[1] == 'FR' or list[1] == 'AU':
            available = True
        else:
            available = False
        body = json.dumps(dict(name=list[0], alpha_2=list[1], alpha_3=list[2], available=available))
        print("Sending Data about: {}".format(list[0].upper()))
        post = http.request('POST', view,  headers={'Content-Type': 'application/json'}, body=body)
        time.sleep(1)
        print("{} ===> [{}, {}, {}]\n".format(list[0], list[1], list[2], available))
    except IndexError:
        pass
