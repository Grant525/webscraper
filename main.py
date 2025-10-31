import requests 
from bs4 import BeautifulSoup

url =  "https://www.scrapethissite.com/pages/"                                        #"https://sandbox.oxylabs.io/products" for dynamic practice 
page = requests.get(url)
soap = BeautifulSoup(page.text, "html.parser")
#print(soap.prettify())
soap.find("div")