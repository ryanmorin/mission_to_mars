#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

# 1. Use browser to visit the URL 
#theurl = 'https://marshemispheres.com/'
#browser = Browser('chrome', **executable_path, headless=True)
#browser.visit(theurl)

#the url address link that appears in the challenge.
theurl = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

thepage = urllib.request.urlopen(theurl)

bsoup = soup(thepage, features='lxml')

all_imgs = bsoup.find('div', id='product-section')

hem_href_list = [i['href'] for i in all_imgs.find_all('a', href=True)]

hem_names = [h.text.strip() for h in all_imgs.find_all('h3')]


# In[3]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

base_url = 'https://astrogeology.usgs.gov'
hem_jpegs = []

def hem_list():
    for href in hem_href_list:
        url = f'{base_url}{href}'
        thepage = urllib.request.urlopen(url)
        bsoup = soup(thepage, features='lxml')
        jpeg_link = (bsoup.find('li')).find('a').attrs['href']
        hem_jpegs.append(jpeg_link)
    return(hem_jpegs)

hem_jpegs = hem_list()


# In[4]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.

d=dict()

for i in range(len(hem_names)):
    d['title'], d['img_url'] = hem_names[i], hem_jpegs[i]
    hemisphere_image_urls.append(d.copy())


# In[5]:


# 4. Print the list that holds the dictionary of each image url and title.
print(hemisphere_image_urls)


# In[8]:


# 5. Quit the browser


# In[ ]:




