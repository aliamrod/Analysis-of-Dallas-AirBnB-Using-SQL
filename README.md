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

