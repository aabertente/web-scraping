#import python modules and libraries
from configparser import RawConfigParser
from itertools import zip_longest
from operator import ipow
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from asyncore import write
from gettext import find
import urllib.request
from os import link
import requests
import csv

#lists varaibles
job_titles_list = []
job_titles_list = []
company_name_list = []
logo_list = []
location_name_list = []
publish_date_list = []
links = []
salary = []

#requests data from from page using url
result = requests.get("https://www.linkup.com/search/results/Python-Developer-jobs?location=parsippany%2C+nj")

#save page centent page
src = result.content
#print(src)

#create soup object to parse centent
soup = BeautifulSoup(src, "html.parser")
print(soup)

#find the elements that we looking for | #class_=['css-4c4ojb', 'css-do6t5g']
job_titles = soup.find_all("div", {"class":"col s12"}).find('h4')
company_name = soup.find_all("span", {"class":"semi-bold"})
location_name = soup.find_all("span", {"class":"vertical-bar semi-bold"})
publish_date = soup.find_all("div", {"class":"row job-listing"})

#get clear data from the append string function
for i in range(len(job_titles)):
    job_titles_list.append(job_titles[i].text)
    company_name_list.append(company_name[i].text)
    location_name_list.append(location_name[i].text)
    publish_date_list.append(publish_date[i].text)
    #links.append("https://url.com"+job_titles[data].find("a").attrs['href'])
print(job_titles)
#for link in links:
 #   result = requests.get(link)
 #   src = result.content
 #   soup = BeautifulSoup(src, "lxml")
 #   salaries = soup.find("div", {"class":"css-rcl8e5"}).find("span", {"class":"css-4xky9y"})
 #   salary.append(salaries) 

#create csv file to save my scraping date
file_list = [job_titles_list, company_name_list, location_name_list, publish_date_list, links, salary]
exported = zip_longest(*file_list)
with open("/home/abdellahpc/Bureau/Python/_Python_programes/jobs_casa_data.csv", "w") as data_file:
    mywriter = csv.writer(data_file)
    mywriter.writerow(["Job title", "Company name", "Company location", "Pubish date", "links", "Salary"])
    mywriter.writerows(exported)