#importing of all libraries that we need
from contextlib import nullcontext
from itertools import zip_longest
from unittest import result
from bs4 import BeautifulSoup
import requests
import csv

#request page from any url
result = requests.get("https://www.imdb.com/list/ls029217360/")
#save page centent on varaible 'src'
src = result.content
#create soup object to parse centent
soup = BeautifulSoup(src, "html.parser")
movie_name = []                
year_list = []
certificate_list = []
runtime_list = []
genre_list = []
rating_list = []
#start to getting page elements content
base = soup.find('div', class_="lister")
rating_div = base.find_all('div', class_="ipl-rating-star small")
span = base.find_all('h3', class_="lister-item-header")
certificate = base.find_all('span', class_="certificate")
runtime = base.find_all('span', class_="runtime")
genre = base.find_all('span', class_="genre")
#This for loop to getting page elements one by one, and them to the empty list
for l in range(len(span)):
    movie_title = span[l].find("a")
    movie_name.append(movie_title.text)
    year = span[l].find('span', class_="lister-item-year")
    year_list.append(year.text)
    genre_list.append(genre[l].text.strip())

#These elements are processed alone because the number of return values is limited
for i in range(len(runtime)):
    runtime_list.append(runtime[i].text)
for i in range(len(rating_div)):
    rating = rating_div[i].find('span', class_="ipl-rating-star__star")
    rating_list.append(rating.text)
for i in range(len(certificate)):
    certificate_list.append(certificate[i].text)

print(movie_name)
print(year_list)
print(certificate_list)
print(runtime_list)
print(genre_list)
#All data obtained was saved on separate file '.csv'
file_list = [movie_name, year_list, certificate_list, runtime_list, genre_list]
exported = zip_longest(*file_list)
with open("/home/abdellahpc/Bureau/Python/Scraping/web_scraping-movies/movies_data.csv", "w") as data_file:
    mywriter = csv.writer(data_file)
    mywriter.writerow(["Movie name", "Year of production", "Certificate", "Run time", "Genre"])
    mywriter.writerows(exported)
