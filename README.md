# Mission to Mars

## Purpose
Use BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

### Deliverable 1
Scrape Full-Resolution Mars Hemisphere Images and Titles.

1. Code is written that retrieves the full-resolution image and title for each hemisphere image.
![title](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/title.png)

2. The full-resolution images of the hemispheres are added to the dictionary.
![images](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/jpegs.png) 

3. The titles for the hemisphere images are added to the dictionary.
![titles](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/dictionary.png)

4. The list contains the dictionary of the full-resolution image URL string and title for each hemisphere image.
![names_+_url](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/dictionary.png)

This code is found in `Mission_to_Mars_Challenge.py`

### Deliverable 2
Update the Web App with Mars’s Hemisphere Images and Titles 

1. The `scraping.py` file contains code that retrieves the full-resolution image URL and title for each hemisphere image.
![scrape](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/import_m2m_scrape.png)

2. The Mongo database is updated to contain the full-resolution image URL and title for each hemisphere image.
![mongo](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/data_from_mongo.png) 

3. The `index.html` file contains code that will display the full-resolution image URL and title for each hemisphere image.
![index](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/images_to_html.png)

4. After the scraping has been completed, the web app contains all the information from this module and the full-resolution images and titles for the four hemisphere images.
![working_site](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/working_web_page.png)

### Deliverable 3
Update the Web App with Mars’s Hemisphere Images and Titles 

1. The webpage is mobile-responsive.
I added `col-sm-12` to the div class
![mobile](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/mobile_resp.png)

2. Two additional Bootstrap 3 components are used to style the webpage.
  a. Change Jumbotron background
  ![background](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/backgnd.png)
  
  b. Change button color
  ![color_btn](https://github.com/ryanmorin/mission_to_mars/blob/main/screen_shots/chng_btn.png)
