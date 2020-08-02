from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=['GET'])
def API():
    url = "https://www.worldometers.info/coronavirus/"
    respo = requests.get(url)
    print(respo)
    html = respo.content
    soup = BeautifulSoup(html, 'html.parser')
    live_data = soup.find_all('div', id='maincounter-wrap')
    for i in live_data:
        print(i.text)

    #table_data = soup.find_all('table',id="main_table_countries_today")

    table_body = soup.find('tbody')
    table_row = table_body.find_all('tr')
    countries = []
    cases=[]
    todays = []
    deaths = []

    for tr in table_row:
        td = tr.find_all('td')
        countries.append(td[0].text)
        cases.append(td[1].text)
        todays.append(td[2].text)
        deaths.append(td[3].text)


    indexdata = [i for i in range(1,len(countries)+1)]
    headers = ['countries','Total cases','today cases','deaths']
    df = pd.DataFrame(list(zip(countries,cases,todays,deaths)),columns=headers,index=indexdata)
    print(df)





if __name__ == '__main__':
    app.run()
