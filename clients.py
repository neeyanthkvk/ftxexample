import time

from rest.client import FtxClient
from websockets.client import FtxWebsocketClient

api_key = 'API_KEY'
secret = 'API_SECRET'

def main():
    rest_client = FtxClient(api_key, secret)
    websocket_client = FtxWebsocketClient(api_key, secret)
    websocket_client.connect()
    while(True):
        time.sleep(2)
        print(websocket_client.get_orderbook('BTC/USD'))
        print(rest_client.get_orderbook('BTC/USD', depth=1))

if __name__ == '__main__':
    main()
