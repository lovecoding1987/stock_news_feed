from dotenv import load_dotenv
load_dotenv()
import os
from newsapi import NewsApiClient
import requests
import json
# Init
#import winsound
#import sqlite3
duration = 1000  # milliseconds
freq = 440  # Hz
import pyfiglet


import time

data = ["AAPL","SQ","PLTR","MSFT","Z","QQQ","SPY","ARKK","TSLA","GME","BABA"]

stock_token=os.environ.get("stock_token")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text +' ff /n')



def menu():
    ascii_banner = pyfiglet.figlet_format("NEWS TRACKER PILOT PROGRAM")
    print(ascii_banner)

    for i in data:
        print(i)

    print (' would you like to add stocks to monitor ')
    a = input()

    if a == 'yes':
        print (' Enter stock ticker symbol ')
        b = input()

        data.append(b)
        print (data )
        print("would you like to start monitoring news for these stocks ? type Y/N ")
        c = input()
    if c == 'Y':
        print("starting monitoring for " , data)
        main()

    if c == 'N':

        system.exit()




def main():
    while True:
        data_str = ",".join(data)


        url =  f"https://stocknewsapi.com/api/v1?tickers={data_str}&items=50&date=today&token={stock_token}"
        print(url)
        response = requests.get(url)
        if len(response.json()['data'])== 0:

            print("no data")

        else:

            for i in range( len( response.json()['data'] )):

                jprint(response.json()['data'][i]['date'] +  '******************************************************************        '' title : ' + response.json()['data'][i]['title'] + "************************** news******************************* " +  response.json()['data'][i]['text'] +  " *********************sentiment************************* " + response.json()['data'][i]['sentiment'] )
                #winsound.Beep(freq, duration)


        time.sleep(3)


main()
