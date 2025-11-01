import requests 
from bs4 import BeautifulSoup
import pandas as pd

def webscraper(site):
    url = site                                    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

def clean_data(soup):
    t_titles = soup.find_all("th")
    table_titles = [titles.get_text(strip=True) for titles in t_titles]
    table_titles.pop(0)
    info_data = soup.find_all("td")
    info_txt = [info.get_text(strip=True) for info in info_data]
    return info_txt, table_titles
    
def get_rows(info_txt,width):
    data = []
    start = 0
    end = len(info_txt) + 1
    while start + width < end:
        data.append(info_txt[start:start + width])
        start+=width
    return data 

def rid_of_numbers(data):
    for d in data:
        d.pop(0)
    return data 

def create_df(data, table_titles):
    df = pd.DataFrame(data, columns = table_titles)
    return df 

def main():
    raw_data = webscraper("https://stockanalysis.com/list/highest-revenue/")
    cleaned_data, titles = clean_data(raw_data)
    width = len(titles) + 1
    rows = get_rows(cleaned_data,width)
    data = rid_of_numbers(rows)
    df = create_df(data, titles)
    print(df)

main()