#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request


# In[ ]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[ ]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[ ]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[ ]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[ ]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[2]:


# 1. Use browser to visit the URL 
#theurl = 'https://marshemispheres.com/'

theurl = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
thepage = urllib.request.urlopen(theurl)

bsoup = soup(thepage)

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
        bsoup = soup(thepage)
        jpeg_link = (bsoup.find('li')).find('a').attrs['href']
        hem_jpegs.append(jpeg_link)
    return(hem_jpegs)

hem_jpegs = hem_list()


# In[4]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.

d=dict()

def retrieve_img_urls():
    for i in range(len(hem_names)):
        d['name'], d['jpeg'] = hem_names[i], hem_jpegs[i]
        hemisphere_image_urls.append(d.copy())
    return hemisphere_image_urls


# In[5]:


# 4. Print the list that holds the dictionary of each image url and title.
print(retrieve_img_urls())


# In[ ]:


# 5. Quit the browser
#browser.quit()


# In[ ]:




