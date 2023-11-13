## $ pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape AirBnB listings.
def scrape_airbnb_listings():
  url = 'https://www.airbnb.com/s/Dallas--Texas--United-States/homes?adults=2'
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')

# Extract relevant information from webpage
# Extracting listing titles...
listings = soup.find_all('div', class_ = '_8ssblpx')
titles = [listing.find('meta', itemprop = 'name')['content'] for listing in listings]

# Write data to CSV file. 
with open('listings.csv', 'w', newline='', encoding='utf-8') as csvfile:
  filednames = ['Title']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()

  for title in titles:
    writer.writerow({'Title': title})

# Call the function to scape AirBnB listings.
    scrape_airbnb_listings()

