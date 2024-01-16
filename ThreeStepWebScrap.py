from bs4 import BeautifulSoup
from re import sub
import requests as r
import pandas as pd

URL = 'https://requests.readthedocs.io/en/latest/api/'

word_list = []
new_list = []

if 'http' not in URL:
    URL = 'https://' + URL
response = r.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
content = soup.text

content = content.split(' ')
for word in content:
    if word != '' and len(word) >= 2:
        word = sub('[^A-Za-z0-9]+', '', word)
        new_list.append(word)

data = pd.DataFrame(new_list)
data = data.value_counts()
print(data)
