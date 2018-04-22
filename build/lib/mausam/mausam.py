import datetime
import requests

from bs4 import BeautifulSoup
import pandas as pd


def fetch_weather():

    """Grab data from Meteorological Forecasting Division (MFD), Nepal"""

    url = "http://www.mfd.gov.np/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    right_table=soup.find('table', class_='table')
    return right_table

def main():
    
    A=[]
    B=[]
    C=[]
    D=[]

    for row in fetch_weather().findAll("tr"):
        cells = row.findAll('td')
        if len(cells)==4:
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))


    df=pd.DataFrame(A,columns=['Station'])
    df['Max']=B
    df['Min']=C
    df['Rain']=D

    show_date = []
    today = datetime.date.today()
    show_date.append(today)
    print("Today's Date: ", show_date[0])

    print(df)   

if __name__ == '__main__':
    main()
