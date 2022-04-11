from email.headerregistry import Address
from itertools import zip_longest
from multiprocessing import Condition
from unittest import result
from bs4 import BeautifulSoup
import requests
import csv
import re

allsites = ["https://estem.ma/",
            "http://www.aui.ma/en/",
            "http://www.elbiliasup.ma/",
            "https://emcgi.ma/",
            "https://www.emsi.ma/",
            "http://www.esjc.ma/",
            "https://ecoleheec.ma/",
            "https://istl.ma/",
            "https://ueuromed.org/",
            "https://hem.ac.ma/",
            "https://www.eigsica.ma/",
            "https://www.esca.ma/"]
            #"https://www.uir.ac.ma/"
emails = []
phones = []
for l in allsites:
    result = requests.get(l)
    soup = BeautifulSoup(result.content, "lxml")
    for link in soup.find_all('a', attrs={'href': re.compile("^mailto:")}):
        emails.append(link.get('href'))
    for tele in soup.find_all('a', attrs={'href': re.compile("^tel:")}):
        phones.append(tele.get('href'))
    #emails.append('\n') # !
print(emails)
print(phones)

file_list = [emails, phones]
exported = zip_longest(*file_list)
with open("/home/abdellahpc/Bureau/Python/Scraping/web_scraping-emails-phones/mydata.csv", "w") as data_file:
    mywriter = csv.writer(data_file)
    mywriter.writerow(["Emails", "Phones"])
    mywriter.writerows(exported)
