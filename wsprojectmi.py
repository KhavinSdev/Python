#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import lxml
import bs4
import requests


# In[ ]:


# request = requests.get('https://books.toscrape.com/catalogue/page-1.html')


# In[ ]:


# wscrape = bs4.BeautifulSoup(request.text, 'lxml')


# In[ ]:


# for i in range(len(wscrape.select('.image_container'))):
#     print(wscrape.select('.image_container')[i].select('img')[0]['alt'])


# In[ ]:


# pageno = wscrape.select('.current')


# In[ ]:


# pageno[0].text


# In[ ]:


sf = int(input('How many pages of the shop would you like to view the titles?' + ' '))

for pg in range(sf + 1):
    request = requests.get(f'https://books.toscrape.com/catalogue/page-{pg}.html')
    wscrape = bs4.BeautifulSoup(request.text, 'lxml')
    for i in range(len(wscrape.select('.image_container'))):
        print(wscrape.select('.image_container')[i].select('img')[0]['alt']) 


# In[ ]:




