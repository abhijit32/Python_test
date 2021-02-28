from bs4 import BeautifulSoup
import re
import requests
import database
import time

RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

allbooks_locator = 'section ol.row li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
page_locator = 'ul.pager li.current'

url = 'https://books.toscrape.com/'
soup = BeautifulSoup(requests.get(url).content,'html.parser')

page_range = soup.select_one(page_locator).string.strip()
regex_pattern_page_range = 'Page 1 of ([0-9]+)'

total_pages = int(re.match(regex_pattern_page_range,page_range).group(1))

start = time.time()
print('Started...')

database.clearBooks()


for page in range(total_pages+1):
    catalogue = f"catalogue/page-{page}.html"
    page_url = url + catalogue
    page_soup = BeautifulSoup(requests.get(page_url).content,'html.parser')
    allBooks = page_soup.select(allbooks_locator)

    
    for book in allBooks:
        name = book.find('h3').contents[0].attrs['title']
        rating_text = book.find(class_='star-rating').attrs['class'][1]
        rating = int(RATINGS[rating_text])
        price = book.find(class_='price_color').string    

        database.insertBooks(name,rating,price)

end = time.time()

print(f"Script finished in {end-start} seconds")
    
    
    


