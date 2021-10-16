# GET Forms

import requests
from bs4 import BeautifulSoup
content = requests.get("https://www.imdb.com/find?q=Mark&s=nm&exact=true&ref_=fn_nm_ex")
doc = BeautifulSoup(content.text, 'html.parser')
# Grab all of the titles
name_tags = doc.find_all(class_="result_text")

# Let's print the first 5
for name in name_tags:
    print(name.a.string)

# Submitting POST Forms

response = requests.get("https://search.dca.ca.gov/results")
doc = BeautifulSoup(response.text, 'html.parser')

# Grab all of the rows
name_tags = doc.find_all("h3")

# Let's print the first 5
for name in name_tags:
    print(name.text)

print(response.text)

data = {
    'lastName': 'Kelly',
    'firstName': 'John',
    'boardCode': '9',
    'licenseNumber': '',
    'licenseType' : '250',
    'registryNumber': ''
}

url = "https://search.dca.ca.gov/results"

response = requests.post(url, data=data)
doc = BeautifulSoup(response.text, 'html.parser')

# Grabbing all the name tags
name_tags = doc.find_all("h3")

# Let's print the first 5
for name in name_tags:
    print(name.text)