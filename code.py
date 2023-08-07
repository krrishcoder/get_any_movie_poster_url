import requests
import re
from bs4 import BeautifulSoup
from googlesearch import search

#year of release  --> done
#duration of movie  -->done  done
#starring   -->done done
#director  --> done done
#genres   --> done by just watch
#short summary --> done by justwatch

query = "Waltair Veerayya /justwatch "
url = ""

my_results_list = []

for i in search(query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = 10,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = None,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
               ):
    #my_results_list.append(i)
    if("https://www.justwatch.com/" in i):
      url  = i
      break

response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, "lxml")
    # Example: Extract all the links on the page

    div_class = 'picture-comp title-poster__image'
    div_ = soup.find_all('picture', class_=div_class)
    for i in div_:
      for j in i.children:
        input_string = j.attrs['data-srcset']
        substring = input_string.split(',')[0].strip()
        print(substring)
        break
      break  
   
   
      
        






