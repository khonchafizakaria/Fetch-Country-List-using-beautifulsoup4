import urllib3
import json
import time
from bs4 import BeautifulSoup as bs

url = 'https://www.nationsonline.org/oneworld/country_code_list.htm'

# URL Endpoints
view = '<django_view_url>'

http = urllib3.PoolManager()

rs = http.request('GET', url)

# Our Fetched Data
soup = bs(rs.data, features='html5lib')

# loop over each table row <tr>
for i in soup.find_all('tr'):
    
    # in each table row, we will loop over each table cell <td>
    tds = i.find_all('td')
    
    # create a list of table cells
    list = [j.text.strip() for j in tds if j is not None]
    
    # the first cell is for icons, we don't need it
    del list[0]
    
    # This website is sorting countries by name, and each Letter has its own row
    # IndexError is imminent, counter it in the except block
    try:
        
        # You can remove this if statement if you don't need it.
        if list[1] in ['GB', 'US', 'CA', 'FR', 'MA']:
            available = True
        else:
            available = False
           
        # The Body of my request is constructed according to my needs, adjust it to yours.
        body = json.dumps(dict(name=list[0], alpha_2=list[1], alpha_3=list[2], available=available))
        print("Sending Data about: {}".format(list[0].upper()))
        
        post = http.request('POST', view,  headers={'Content-Type': 'application/json'}, body=body)
        
        # Sleep function 
        # The process will take around 247 secondes ~ 4.1 minutes, ommit the sleep function to accelerate.
        time.sleep(1)
        
        print("{} ===> [{}, {}, {}]\n".format(list[0], list[1], list[2], available))
        
        # Check views.py to see how to catch post data.
        
    except IndexError:
        pass
