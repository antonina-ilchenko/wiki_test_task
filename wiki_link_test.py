
from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint

def is_it_wiki_link(link):
    fmt = "https://.{2}\.wikipedia\.org/wiki/(.*)"
    result = re.match(fmt, link)
    return result is not None

def validation_wiki_link(link):
    if is_it_wiki_link(link):
        try:
            response = requests.get(link)
        except:
            raise RuntimeError("The link format is OK, but request failed")
        if response.status_code != 200:
            raise RuntimeError('Wrong status code') 
    else:        
        raise RuntimeError('Web site does not exist') 
 
def range_iteration():
    while True:
        try:
            n = int(input('Enter itaretion number, from 1 to 20:'))
            if n >= 1 and n <= 20:
                print('ok')
                return n
            else:
                print("!!! Should be Interger number between 1 to 20") 
        except ValueError:
            print("!!!Invalid format. Should be Interger number between 1 to 20")

def create_full_url(link):
    base_url='https://en.wikipedia.org'
    return base_url+link
    
def has_wiki(link):
    fmt = "/wiki/(.*)"
    result = re.match(fmt, str(link))
    return result is not None

def find_all_wiki_link_on_page(link):
    response = requests.get(link).content
    soup = BeautifulSoup(response, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        if has_wiki(a["href"]):
            links.append(create_full_url(a["href"]))
    return list(set(links))        

def input_link():
    while True:
        wiki_link = input('Enter any link to WIKIPEDIA:')
        try:
            validation_wiki_link(wiki_link)
            return wiki_link
        except RuntimeError as e:
            print(e)


# # Set  parameters in the code
# wiki_link = 'https://en.wikipedia.org/wiki/Python'
# validation_wiki_link(wiki_link)
# n = 1

# Get up parameters from consol
wiki_link = input_link()
n = range_iteration()

original_links = find_all_wiki_link_on_page(wiki_link)
total = [original_links]

for i in range(n):
    total.append([])
    print(f"\nCycle {i+1}\n")
    print(f"Need to get {len(total[i])} links\n")
    for link in total[i]:
        print(f"Working on {link}")
        wiki_links = find_all_wiki_link_on_page(link)
        print(f"Found {len(wiki_links)} links")
        total[i + 1] = total[i + 1] + wiki_links
    total[i + 1] = list(set(total[i+1]))

flat_list = []
for sublist in total:
    for item in sublist:
        flat_list.append(item)

unique_list = set(flat_list)
pprint(unique_list)
print(f"Total count unique links: {len(unique_list)} \n")




