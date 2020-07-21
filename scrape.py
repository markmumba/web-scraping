from bs4 import BeautifulSoup
import requests 
 
source =requests.get('https://markmumba.github.io/apple-music/').text

soup =BeautifulSoup(source ,'lxml')

features =soup.find('div', id='offer')

 #print (features.prettify())

headline =features.h3.text
print(headline)


    