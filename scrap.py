import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

class Scrap:

    def get_data():

        url = os.getenv('SCRAP_URL')
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.text, 'html.parser')

        table = soup.find("table", attrs={"id":"BluePromedio"})
        title = table.find("td", attrs={"class":"colNombre"}).text
        date = table.find("td", attrs={"class":"colFecha"}).text
        
        buy = table.find_next("td", attrs={"class":"colCompraVenta"}).contents
        sell = table.find_previous("td", attrs={"class":"colCompraVenta"}).contents

        variation = table.find("td", attrs={"class":"colVariacion"}).text

        data = {
            'title': title,
            'date': date,
            'values' : {
                'buy': buy[0],
                'sell': sell[0]
            },
            'variation': variation
        }

        return data


        

    
    
