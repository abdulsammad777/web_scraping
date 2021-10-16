# import required libraries

import requests
from lxml import html
from bs4 import BeautifulSoup

# login and to-scrape URL

login_url = "http://quotes.toscrape.com/login"
get_url = "http://quotes.toscrape.com/"

# session object

session_req = requests.session()

# getting the CSRF token

login = session_req.get(login_url)

login_html = html.fromstring(login.content)
authenticity_token = list(set(login_html.xpath("//input[@type='hidden']/@value")))[0]

print(authenticity_token)

payload = {
    "username": "pratheerth",
    "password": "password",
    "csrf_token": authenticity_token
}

# POST request

post = session_req.post(
    login_url,
    data = payload
)

# Getting the required page

result = session_req.get(
    get_url
)

soup = BeautifulSoup(result.text, 'html.parser')
pint(soup)