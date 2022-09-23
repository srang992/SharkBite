import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

if __name__ == '__main__':
    def read_web_table(url, table_s_no):
        url = url
        r = requests.get(url)
        bs = soup(r.content, 'html')
        table = bs.find_all('#fullArticle > table')[table_s_no]

        df = pd.read_html(str(table))[0]
        return df
