import time

from rest.client import FtxClient
from websockets.client import FtxWebsocketClient

api_key = 'API_KEY'
secret = 'API_SECRET'
subaccount_name = 'YOUR_SUBACCOUNT_NAME'

def main():
    rest_client = FtxClient(api_key, secret, subaccount_name)
    
    # a request that actually requires proper login credentials to get
    print(rest_client.get_account_info())


if __name__ == '__main__':
    main()
