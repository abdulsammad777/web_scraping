import requests

url = "https://chatapi.p.rapidapi.com/qr_code"

headers = {
    'x-rapidapi-key': "e714bb604fmsha43949ba0de83c6p13f6f4jsn393bf29d206f",
    'x-rapidapi-host': "chatapi.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)