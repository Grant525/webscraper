import requests 
from bs4 import BeautifulSoup
import pandas as pd


url =  "https://stockanalysis.com/list/highest-revenue/"                                        #"https://sandbox.oxylabs.io/products" for dynamic practice 
page = requests.get(url)
soap = BeautifulSoup(page.text, "html.parser")
#print(soap.prettify())
table = soap.find("table", id="main-table")
t_titles = soap.find_all("th")
table_titles = [titles.get_text(strip=True) for titles in t_titles]
data_frame = pd.DataFrame(columns = table_titles)
info_data = soap.find_all("td")
info_txt = [info.get_text(strip=True) for info in info_data]
print(info_txt)