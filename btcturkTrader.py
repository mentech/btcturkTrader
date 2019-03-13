from btcturk import Btcturk
import time,requests

client=Btcturk('2522224-f732-44348-9358-3555fd4fdb1','0keadfzWS345qBzlBdfGNUmy5dbpn')
TelegramUrl="https://api.telegram.org/bot7444937:AAsrgvweYxrKwerwrwj1X_Ffwwrgw/sendMessage?chat_id=4436344&text="

class btcTry(object):
    alis = 0.1
    alisMik=0.1
    satis = 0.1
    satisMik = 0.1
class btcUsdt(object):
    alis = 0.1
    alisMik=0.1
    satis = 0.1
    satisMik = 0.1
class usdtTry(object):
    alis = 0.1
    alisMik=0.1
    satis = 0.1
    satisMik = 0.1

def fiyatlariCek():
  try:
    alsatlar= client.get_order_book(pair_symbol="btctry")
    btcTry.alis=float(alsatlar["bids"][0][0])
    btcTry.alisMik=float(alsatlar["bids"][0][1])
    btcTry.satis=float(alsatlar["asks"][0][0])
    btcTry.satisMik=float(alsatlar["asks"][0][1])

    alsatlar= client.get_order_book(pair_symbol="btcusdt")
    btcUsdt.alis=float(alsatlar["bids"][0][0])
    btcUsdt.alisMik=float(alsatlar["bids"][0][1])
    btcUsdt.satis=float(alsatlar["asks"][0][0])
    btcUsdt.satisMik=float(alsatlar["asks"][0][1])

    alsatlar= client.get_order_book(pair_symbol="usdttry")
    usdtTry.alis=float(alsatlar["bids"][0][0])
    usdtTry.alisMik=float(alsatlar["bids"][0][1])
    usdtTry.satis=float(alsatlar["asks"][0][0])
    usdtTry.satisMik=float(alsatlar["asks"][0][1])
    time.sleep(0.15)
  except:
    print("hata")
    time.sleep(0.15)
    fiyatlariCek()

def btcAlUsdtSat():
  para=100.0
  btc=100/btcTry.satis
  usdt=btc*btcUsdt.alis
  para=usdt*usdtTry.alis
  print(para)
  if para>101:
    requests.get(TelegramUrl+"btcAlUsdSat :"+str(para))

def usdtAlBtcSat():
  para=100.0
  usdt=100/usdtTry.satis
  btc=usdt/btcUsdt.satis
  para=btc*btcTry.alis
  print(para)
  if para>101:
    requests.get(TelegramUrl+"usdtAlBtcSat :"+str(para))
    
while 0<1:
  fiyatlariCek()
  btcAlUsdtSat()
  usdtAlBtcSat()

