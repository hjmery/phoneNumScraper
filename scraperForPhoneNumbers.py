import pandas as pd
import requests
import bs4
import re
import csv

def get_phone(soup):
    # try:
    #     phone = soup.select("a[href*=callto]")[0].text
    #     return phone
    # except:
    #     pass

    phone = []

    try:
        phoneTry = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', response.text)
        for i in phoneTry:
            phone.append(i)
    except:
        pass

    try:
        phoneTry = re.findall(r'(\d\d\d\d\d\d\d\d\d\d)', response.text)
        for i in phoneTry:
            phone.append(i)
    except:
        pass

    try:
        phoneTry = re.findall(r'(\(\d\d\d\) \d\d\d-\d\d\d\d)', response.text)
        for i in phoneTry:
            phone.append(i)
        return phone
    except:
        pass

    try:
        phoneTry = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response.text)[-1]
        for i in phoneTry:
            phone.append(i)
    except:
        return phone

    return phone

def get_email(soup):
    try:
        email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response.text)[-1]
        return email
    except:
        pass

    try:
        email = soup.select("a[href*=mailto]")[-1].text
    except:
        print ('Email not found')
        email = ''
        return email

phone = []

url = 'https://www.provo.org/city-services/airport'
try:
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
except:
    print ('Unsucessful: ' + str(response))

phone = get_phone(soup)
print(soup)
print(phone)

guestFile = open("output.csv","a")

for entries in phone:
    guestFile.write(entries)
    guestFile.write("\n")

guestFile.close()