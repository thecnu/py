import requests
import time 
from datetime import datetime
import pandas as pd 
import pytz


print()
print("başlangıç zamanı")
print()

day = int(input("lütfen günü giriniz: "))
month = int(input("lütfen ayı giriniz: "))
year = int(input("lütfen yılı giriniz: "))

print()
print("bitiş zamanı")
print()
#buraya if else yaz yanlış tarih için...
daya = int(input("lütfen günü giriniz: "))
montha = int(input("lütfen ayı giriniz: "))
yeara = int(input("lütfen yılı giriniz: "))

timea = datetime(year, month, day)
timeb = datetime(yeara, montha, daya)

start_time = int(timea.timestamp())
end_time = int(timeb.timestamp())

symbol = input("Lütfen sembol giriniz: ").upper() + "TRY"
interval = input("Lütfen istediğniz aralığı giriniz (m-h-D) : ") 

urla = "https://api.binance.com/api/v3/klines?symbol"
url = f"{urla}={symbol}&interval={interval}&startTime={start_time}000&endTime={end_time}000"

response = requests.get(url)

data = response.json()


df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
rename = {'timestamp': 'time'}
df = df.rename(columns=rename)

yeni_df = ['time', 'open', 'high', 'low', 'close', 'volume']
yeni_df = df[yeni_df]
yeni_df['time'] = pd.to_datetime(yeni_df['time'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('Europe/Istanbul')
#yardım aldığım tek kısım... buraya az çalış

yeni_df = yeni_df.set_index('time')
yeni_df.index = yeni_df.index.tz_localize(None)

print(yeni_df)
yeni_df.to_excel("ss.xlsx", index=True)

