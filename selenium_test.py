from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait 

browser = webdriver.Chrome(executable_path='C:\\Users\\abhij\\Workspace\\chromedriver_win32\\chromedriver')

Locator = {
    'AUTHOR_DROPDOWN' : 'select#author',
    'TAG_DROPDOWN' : 'select#tag',
    'TAG_DROPDOWN_OPTION' : 'select#tag option[value]',
    'SEARCH_BUTTON' : 'input[name="submit_button"]',
    'CONTENT' : 'span.content',
    'AUTHOR' : 'span.author',
}

browser.get('https://quotes.toscrape.com/search.aspx')

author_dropdown = Select(browser.find_element(By.CSS_SELECTOR, Locator['AUTHOR_DROPDOWN']))
author_dropdown.select_by_visible_text('Albert Einstein')



WebDriverWait(browser,20).until(
    expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, Locator['TAG_DROPDOWN_OPTION'])
    ) 
)

tags_dropdown = Select(browser.find_element(By.CSS_SELECTOR, Locator['TAG_DROPDOWN']))
tags_dropdown.select_by_visible_text('change')

browser.find_element(By.CSS_SELECTOR, Locator['SEARCH_BUTTON']).click()
quote = browser.find_element(By.CSS_SELECTOR, Locator['CONTENT'])

print(quote.text)

pass
