from email.headerregistry import Address
from itertools import zip_longest
from unittest import result
from bs4 import BeautifulSoup
import requests
import csv
import re

allsites = ["https://estem.ma/",
            "https://estem.ma/"]
emails = []
phones = []
for l in allsites:
    result = requests.get(l)
    soup = BeautifulSoup(result.content, "lxml")
    for link in soup.find_all('a', attrs={'href': re.compile("^mailto:")}):
        emails.append(link.get('href'))
    for i in range(1):
        for tele in soup.find_all('a', attrs={'href': re.compile("^tel:")}):
            phones.append(tele.get('href'))
        phones.append('\n')
print(emails)
print(phones)

file_list = [emails, phones]
exported = zip_longest(*file_list)
with open("/home/abdellahpc/Bureau/Python/Scraping/data.csv", "w") as data_file:
    mywriter = csv.writer(data_file)
    mywriter.writerow(["Emails", "Phones"])
    mywriter.writerows(exported)
