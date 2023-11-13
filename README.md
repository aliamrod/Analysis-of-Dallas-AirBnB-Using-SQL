# Analysis-of-Dallas-AirBnB-Using-SQL

## Overview
As someone who is interested in Data Engineering and Data Analytics, I decided to take up a project concerning AirBnB datasets (http://insideairbnb.com). 
Naturally, I thought it would be a good idea to take a look at the data pertaining to my base city of Dallas and see what interesting markers I could find. 

The data was cleaned and EDA in SQL was consequently performed before moving on to visualizing my findings with Tableau.

Tools Used: MySQL, MySQL Workbench, Python, WinZip


## Data Source
To extract preliminary data from AirBnB, web scraping is performed. In the siplest of terms, web scraping is the process of extracting information from a website and unearthing bits of data hidden within. Web scraping involves writing a script that automates the process of gathering data from a website. The primary objective of this script is to identify the relevant information, extract it, and then consequently save it for further analysis for use. 

The first goal is to create 3 separate CSV files:
* One **listings.csv** file that contains Airbnb listing information and Airbnb host information.

* One **calendar.csv** file that contains property availability information throughout the year

* One **reviews.csv** file that contains Airbnb property reviews information


Here's a basic outline of how I approached web scraping using Python and BeautifulSoup and requests libraries:
- airbnb_webscraper.py:

  ```python
import requests
from bs4 import BeautifulSoup
import csv
  ```

`requests` is used to send HTTP requests to the website, `BeautifulSoup` extracts data out of HTML and XML files, and `csv` is the assumed module for reading and writing CSV files.

The class name `_8ssblpx` in the code `soup.find_all('div', class_='_8ssblpx')` is a specific CSS class assigned to certain HTML elements on the Airbnb website. In web development, classes are used to apply styles or identify specific elements using CSS (Cascading Style Sheets) or JavaScript.

In the context of web scraping with BeautifulSoup, the class name is used to target specific HTML elements that have that class assigned. When you inspect the HTML structure of a webpage using browser developer tools, you'll find elements with various classes, IDs, and other attributes.

In the provided code, `soup.find_all('div', class_='_8ssblpx')` is looking for all `div` elements with the class `_8ssblpx`. This is likely done to target a specific section of the Airbnb webpage where listing information is contained. It's important to note that class names like `_8ssblpx` are subject to change if Airbnb updates its website structure, so you may need to inspect the HTML of the specific webpage you are interested in scraping and adjust the class name accordingly.
