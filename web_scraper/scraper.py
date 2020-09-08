import requests
from bs4 import BeautifulSoup
import json

url="https://en.wikipedia.org/wiki/History_of_Mexico"
page=requests.get(url)
# print (page) # print the respone: <Response [200]>
# print (page.text) # print the whole HTML tags of the page
# print (page.content) # print the whole HTML tags of the page

soup=BeautifulSoup(page.content,'html.parser')

def get_citations_needed_count(link):
    counter=[]
    for wrapper in soup.find("div",class_="mw-parser-output").find_all("p"):
        for wrapperw in wrapper.find_all('a', title="Wikipedia:Citation needed"):
            a=wrapperw
            counter.append(a)

    print("How many count citations? \nCount of the Citations =",len(counter))
    return len(counter)    

def  get_citations_needed_report(link):
    for wrapper in soup.find("div",class_="mw-parser-output").find_all("p"):
        for wrapperw in wrapper.find_all('a', title="Wikipedia:Citation needed"):
            a=wrapperw.parent.parent.parent.text.strip()
            print("\n","*"*100,"\n",a,"\n","*"*100,"\n")
    return a

if __name__ == "__main__":
    get_citations_needed_count(url)
    get_citations_needed_report(url)


