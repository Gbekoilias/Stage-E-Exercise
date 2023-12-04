# Import necessary libraries
import requests as r
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
from time import sleep
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
%matplotlib inline
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
#Gatheing the data
urls =[]
years = [str(i) for i in range(2009,2020)] #list of years between 2009-2019
for year in years:
    urls.append (f"https://www.amazon.com/gp/bestsellers/{year}/books")
    urls.append(f"https://www.amazon.com/gp/bestsellers/{year}/books/ref=zg_bsar_pg_2/ref=zg_bsar_pg_2?ie=UTF8&pg=2")
    
urls
#create a function to get the data from the urls
def get_dir(book,year): 
    '''to get the details of each book for each year''' 
    
    import numpy as np
    '''to get the name of price'''

    try:
        price = book.find('span',class_="_cDEzb_p13n-sc-price_3mJ9Z").text[1:]
    except Exception as e:
        price = np.nan
    try:
        ranks = book.find('span', class_='zg-bdg-text').text[1:]
    except Exception as e:
        ranks = np.nan
    try:
        title = book.find('div',class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y").text
    except Exception as e:
        title = np.nan
    try:
        ratings= book.find('span',class_="a-icon-alt").text[:3] 
    except Exception as e:
        ratings = np.nan
    try:
        no_of_reviews  = book.find('span',class_="a-size-small").text
    except Exception as e:
        no_of_reviews = np.nan
    try:
        author = book.find('a',class_="a-size-small a-link-child").text
    except Exception as e:
        author = np.nan
    try:
        cover_type = book.find('span',class_="a-size-small a-color-secondary a-text-normal").text
    except Exception as e:
        cover_type = np.nan
    year = year
    return [price,ranks,title,no_of_reviews,ratings,author,cover_type, year]
#Create a function to get the data from the urls
year = [(str(i),str(i)) for i in range(2009,2020)] 
#create list that contains the a set of each year
years = [j for i in year for j in i] 
#get a list from the above line
years
#Create a for loop to get the data from the urls
for url in urls:  
    website = url 
    driver = webdriver.Chrome()
    driver.get(website)     
    sleep(30)                 
    the_soup = BeautifulSoup(driver.page_source, 'html.parser')           
    books = the_soup.find_all(id = 'gridItemRoot')                 
    all_year.append(books) #add the books to the the list above
    driver.quit()
 #find the length of the list  
len(all_year), len(years)
#Create a list of the books
year_index = (list(enumerate(years)))
dc = year_index
#Create a for loop to get the data from the urls
data = [] 
for i in dc:   
    for books in all_year[i[0]]:             
        for book in books:                 
            data.append(get_dir(book,i[1])) 
 # open file
with open('Amazon.txt', 'w+') as f:
     
    # write elements of list
    for items in data: 
        try:
            f.write('%s\n' %items)
        except Exception as e:
            f.write('%s\n' 'nothing')
     
    print("Success")

# close the file
f.close()
#Read the txt file
amazon_books= pd.DataFrame(data, columns = [
                         'price',
                         'rank',
                         'title',
                         'total_reviews',
                         'ratings',
                         'author',
                       'cover_type',
                          'year'])
#To save to csv file
amazon_books.to_csv('amazon_books_2009-2019.csv')   #To save to csv file
#Read the csv file
amazon_book=pd.read_csv(r"C:\Users\njoku\Documents\Internship\Data_Storytelling\Stage E\amazon_books_2009-2019.csv")
amazon_book.head()