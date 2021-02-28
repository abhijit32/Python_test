from bs4 import BeautifulSoup
import requests
import random
from datetime import datetime
import re

url_home = 'https://www.imdb.com'
url_top250 = 'https://www.imdb.com/chart/top/'
url_search = 'https://www.imdb.com/search/title/'

Locator = {
    'MovieList_top250' : 'div.lister table.chart.full-width tbody.lister-list tr',
    'MovieList_suggestion': 'div.lister-item.mode-advanced'
}

class MovieScrapper:

    def top250Movies(self):

        soup = BeautifulSoup(requests.get(url_top250).content, 'html.parser')

        all_movie_section = soup.select(Locator['MovieList_top250'])
        top_250_movies = []
        for movie_elem in all_movie_section:

            rank = movie_elem.find(class_='titleColumn').next.strip()
            title = movie_elem.find(class_='titleColumn').find('a').string.strip()
            release_year = movie_elem.find(class_='titleColumn').find(class_='secondaryInfo').string.strip()
            rating = movie_elem.find(class_='ratingColumn').find('strong').string.strip()

            top_250_movies.append({'Rank':rank, 'Title':title, 'Year':release_year, 'Rating':rating})
        
        return top_250_movies

    def findMovie(self):
        pass








    



            

 
        

    

    



