import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the IMDb page that we want to scrape.
url = "https://www.imdb.com/chart/top/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Accept-Encoding': 'gzip, deflate',
}

# Make a GET request to the URL.
page = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(page.content, "html5lib")

#Scrape movie year
scraped_years = soup.find_all('span', class_='sc-b85248f1-6 bnDqKN cli-title-metadata-item')

years = []
for year in scraped_years:
    years.append(year.get_text())

# Enumerate over the scraped data
for i, year in enumerate(years):
    # Print every third value until i is 230
    if i <= 228 and i % 3 == 0:
        print(year)
    # Skip 229
    elif i == 229:
        continue
    elif i > 229:
        print(year)
