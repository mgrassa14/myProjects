import requests
import json
import sys
from bs4 import BeautifulSoup
import collections
collections.Callable = collections.abc.Callable
from html.parser import HTMLParser

#declared variables
cookie_input = "ASP.NET_SessionId=do3swwx3jc034sjhg2qzuem1; _ga=GA1.1.219446391.1675964907; _ga_1D6F62T597=GS1.1.1676090470.3.0.1676090470.0.0.0; _ga_EY2MYK54PW=GS1.1.1676401603.12.1.1676401608.0.0.0"


#get file with Filling ID and Name 
def NYFilers():
    fname = "NYFilers.csv"
    try:
        hand = open(fname)
    except:
        print('File cannot be opened:',fname)
        exit()
    lst = list()
    for line in hand:
        fillingID = line.split(",")
    #    print(fillingID)

#this sets the filer ID and will return True when it works
def setFilerID():
    setFilerID_url = "https://publicreporting.elections.ny.gov/CandidateCommitteeDisclosure/GetFilingInventoryData/"
    headers = {"authority": "publicreporting.elections.ny.gov", "accept": "*/*", "accept-language": "en,en-US;q=0.9,it;q=0.8", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", \
        "origin": "https://publicreporting.elections.ny.gov", \
        "referer": "https://publicreporting.elections.ny.gov/CandidateCommitteeDisclosure/CandidateCommitteeDisclosure", \
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", \
        "x-requested-with": "XMLHttpRequest" }
    headers["cookie"] = cookie_input
    payload = {"strFilerId": "100", "strCandidateId": "-+Select+-", "strCommitteeId": "-+Select+-", "searchBy": "FILER", "lstUCOfficeType": "10"}
    r = requests.post(setFilerID_url, headers=headers, data=payload)
    print(r.text)

#Getting filings from server
def getFillings(): 
    getFillings_url = "https://publicreporting.elections.ny.gov/CandidateCommitteeDisclosure/CandidateCommitteeDisclosure"
    headers = {"authority": "publicreporting.elections.ny.gov", \
        "accept": "text/html, */*; q=0.01", \
        "accept-encoding": "gzip, deflate, br", \
        "accept-language": "en,en-US;q=0.9,it;q=0.8", \
        "referer": "https://publicreporting.elections.ny.gov/CandidateCommitteeDisclosure/CandidateCommitteeDisclosure", \
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", \
        "x-requested-with": "XMLHttpRequest" }
    headers["cookie"] = cookie_input
    r = requests.get(getFillings_url, headers=headers)
    #soup is the whole HTML code
    soup = BeautifulSoup(r.content,'lxml')
    #retrieving the data that we want (includes: activity report, date, time, filling ID, & filler ID = the last element)
    for element in soup.findAll('div', attrs = {'class' : 'card-body'}):
        for a in element.findAll("a"):
            print(a['onclick'])
            # fillings.append(a['onclick'])
            # print(fillings)
setFilerID()
getFillings()     


#     a = []
# for i in range(5):
#     # change a = a.append(i) to    
#     a.append(i)
# print(a)
# [0, 1, 2, 3, 4]
    # soup = BeautifulSoup(r.content,'lxml')
    # element = soup.findAll('div', attrs = {'class' : 'card-body'})
    # newH = element[1]
    # soup = BeautifulSoup(newH,'lxml')
    # element2 = soup.find('a')
    # print(element2['onclick'])
    # print(soup)




    # tag = soup.findAll("a")
    #output = tag[1]
    #soup = BeautifulSoup(output,'html.parser')
    #tag = soup.find(
    # print(tag[0])
    #attribute = tag.attrs
  
    # Print the output
    #print(attribute)
    # HTMLParser.handle_starttag(r.content, 'div', [('class', 'card-body')])
    # print(HTMLParser.)
    #print(r.content)
    #[('href', 'https://www.cwi.nl/')]
    #     words = line.split()
    # print(words)
    
    
    #with open("test.txt", "w") as out_file:
    #    out_file.write(str(r.content))

    


