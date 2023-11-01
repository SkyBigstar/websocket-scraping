from websocket import create_connection
import json

headers = json.dumps({
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9,ko;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'Upgrade',
    'Host':'data.tradingview.com',
    'Origin':'https://www.tradingview.com',
    'Pragma':'no-cache',
    'Sec-Websocket-Extensions':'permessage-deflate; client_max_window_bits',
    'Sec-Websocket-Key':'sItJQ1sLedm3As9ZVfxNxw==',
    'Sec-Websocket-Version':'13',
    'Upgrade':'websocket',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
})


ws = create_connection('wss://data.tradingview.com/socket.io/websocket?from=chart%2FLnawPg6F%2F&date=2023_11_01-10_52&type=chart',headers=headers)

# ws.send(json.dumps({"action": "SubAdd", "subs": ["11~BTC", "21~BTC", "5~CCCAGG~BTC~USD", "11~ETH", "21~ETH", "5~CCCAGG~ETH~USD", "11~BCH", "21~BCH", "5~CCCAGG~BCH~USD", 
#                     "11~EOS", "21~EOS", "5~CCCAGG~EOS~USD", "11~XRP", "21~XRP","5~CCCAGG~XRP~USD", "11~LTC", "21~LTC", "5~CCCAGG~LTC~USD", 
#                     "11~ETC", "21~ETC", "5~CCCAGG~ETC~USD", "11~BSV", "21~BSV", "5~CCCAGG~BSV~USD", "11~LINK", "21~LINK", "5~CCCAGG~LINK~USD", "11~ATOM", "21~ATOM", "5~CCCAGG~ATOM~USD"]}))
first = ws.recv()
print(first)
ws.send('''~m~670~m~{"m":"set_auth_token","p":["eyJhbGciOiJSUzUxMiIsImtpZCI6IkdaeFUiLCJ0eXAiOiJKV1QifQ.eyJ1c2VyX2lkIjo2NTkwNTg2NCwiZXhwIjoxNjk4ODY1MTE1LCJpYXQiOjE2OTg4NTA3MTUsInBsYW4iOiIiLCJleHRfaG91cnMiOjEsInBlcm0iOiIiLCJzdHVkeV9wZXJtIjoiIiwibWF4X3N0dWRpZXMiOjIsIm1heF9mdW5kYW1lbnRhbHMiOjAsIm1heF9jaGFydHMiOjEsIm1heF9hY3RpdmVfYWxlcnRzIjoxLCJtYXhfc3R1ZHlfb25fc3R1ZHkiOjEsIm1heF9vdmVyYWxsX2FsZXJ0cyI6MjAwMCwibWF4X2FjdGl2ZV9wcmltaXRpdmVfYWxlcnRzIjo1LCJtYXhfYWN0aXZlX2NvbXBsZXhfYWxlcnRzIjoxLCJtYXhfY29ubmVjdGlvbnMiOjJ9.FbLEBpY8BhWxHC-XZfj0MKyUf89cavWjpaL_oJiVVqscRnFdxoqJ184NIcWX9Arl7cwcj1FFilbfnBRL82648HgrNzB2O1dIxQuXAsODbgpuzPcf5p5RQkcuN-GhMYAy_SNlgWWg0ChIaTsGUsNVmisSr51KW1K957Bf2JbvYSY"]}''')
ws.send('''~m~34~m~{"m":"set_locale","p":["en","US"]}''')
ws.send('''~m~55~m~{"m":"chart_create_session","p":["cs_WQx1zOjZPghi",""]}''')
ws.send('''~m~52~m~{"m":"quote_create_session","p":["qs_xk1JDMkzI2U5"]}''')
ws.send('''~m~432~m~{"m":"quote_set_fields","p":["qs_xk1JDMkzI2U5","base-currency-logoid","ch","chp","currency-logoid","currency_code","currency_id","base_currency_id","current_session","description","exchange","format","fractional","is_tradable","language","local_description","listed_exchange","logoid","lp","lp_time","minmov","minmove2","original_name","pricescale","pro_name","short_name","type","typespecs","update_mode","volume","value_unit_id"]}''')
ws.send('''~m~83~m~{"m":"quote_create_session","p":["qs_snapshoter_basic-symbol-quotes_IyRijXnXu8q9"]}''')
ws.send('''~m~406~m~{"m":"quote_set_fields","p":["qs_snapshoter_basic-symbol-quotes_IyRijXnXu8q9","pro_name","base_name","short_name","description","type","exchange","typespecs","listed_exchange","lp","country_code","provider_id","symbol-primaryname","logoid","base-currency-logoid","currency-logoid","source-logoid","update_mode","source","source2","pricescale","minmov","fractional","visible-plots-set","industry","sector"]}''')
ws.send('''~m~359~m~{"m":"quote_add_symbols","p":["qs_snapshoter_basic-symbol-quotes_IyRijXnXu8q9","###Indices","SP:SPX","TVC:NDQ","TVC:DJI","CBOE:VIX","TVC:DXY","###Stocks","NASDAQ:AAPL","NASDAQ:TSLA","NASDAQ:NFLX","###Futures","TVC:USOIL","TVC:GOLD","TVC:SILVER","###Forex","FX:EURUSD","FX:GBPUSD","FX:USDJPY","###Crypto","BITSTAMP:BTCUSD","BINANCE:BTCUSDT","BITSTAMP:ETHUSD"]}''')
ws.send('''~m~57~m~{"m":"switch_timezone","p":["cs_WQx1zOjZPghi","Etc/UTC"]}''')
#ws.send('''~m~52~m~{"m":"quote_create_session","p":["qs_0ZjvVjRCXuKi"]}''')
#ws.send('''~m~126~m~{"m":"quote_add_symbols","p":["qs_0ZjvVjRCXuKi","={\"adjustment\":\"splits\",\"currency-id\":\"USD\",\"symbol\":\"SP:SPX\"}"]}''')
#ws.send('''~m~135~m~{"m":"resolve_symbol","p":["cs_WQx1zOjZPghi","sds_sym_1","={\"adjustment\":\"splits\",\"currency-id\":\"USD\",\"symbol\":\"SP:SPX\"}"]}''')
#ws.send('''~m~81~m~{"m":"create_series","p":["cs_WQx1zOjZPghi","sds_1","s1","sds_sym_1","D",300,""]}''')
#ws.send('''~m~58~m~{"m":"quote_add_symbols","p":["qs_xk1JDMkzI2U5","SP:SPX"]}''')

# Printing all the result
while True:
    try:
        result = ws.recv()
      #  if (result=='~m~4~m~~h~1'):
      #      ws.send('~m~4~m~~h~1')
        print(result)
    except Exception as e:
        print(e)
        break