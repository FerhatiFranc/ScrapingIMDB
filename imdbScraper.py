import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the IMDb page that we want to scrape.
url = "https://www.imdb.com/chart/top/"

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

# Make a GET request to the URL.
page = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(page.content, "html5lib")
soup.prettify()

# Scrape movie names.
scraped_movies = soup.find_all('h3', class_='ipc-title__text')

movies = []
for movie in scraped_movies:
    movies.append(movie.get_text().strip())

# Remove the first line.
movies = movies[1:]

# Remove the last 12 lines.
movies = movies[:-12]

#prints the top 250 movies
for movie in movies: 
    print(movie)

