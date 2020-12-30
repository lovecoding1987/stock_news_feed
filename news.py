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
import _thread
from twilio.rest import Client



import time

tickers = ["AAPL","SQ","PLTR","MSFT","Z","QQQ","SPY","ARKK","TSLA","GME","BABA"]
tickers_str = ",".join(tickers)

stock_token=os.environ.get("stock_token")

stock_news_url =  f"https://stocknewsapi.com/api/v1?tickers={tickers_str}&items=50&date=yesterday&token={stock_token}"
print(stock_news_url)

twilio_account_sid = os.environ.get("twilio_account_sid")
twilio_auth_token = os.environ.get("twilio_auth_token")
twilio_phone_number = os.environ.get("twilio_phone_number")

twilio_client = Client(twilio_account_sid, twilio_auth_token)

       
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
        


def find_news(news_data, news_url):
    index = -1
    for i in range(len(news_data)):
        item = news_data[i]
        if item['news_url'] == news_url:
            index = i
            break

    return index


def main():
    news = []
    while True:
        response = requests.get(stock_news_url)
        data = response.json()['data']
        for item in data:
            if find_news(news, item['news_url']) == -1:
                news.append(item)
                print(item)
            #winsound.Beep(freq, duration)
            

        time.sleep(60)


def sms(): 
    message = twilio_client.messages.create(
        to="+12513090696", 
        from_=twilio_phone_number,
        body="Hello from Python!")

    print("Twilio message id: " + message.sid)

try:
    _thread.start_new_thread(main, ()) 
except:
    print("Error: unable to start thread")

while 1:
    pass

#main()