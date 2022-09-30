# requires Python >=3.6
# pip install tardis-dev

from tardis_dev import datasets, get_exchange_details
import logging

exchange = 'ftx-us'
exchange_details = get_exchange_details(exchange)
for symbol in exchange_details["datasets"]["symbols"]:
    #data_types = symbol["dataTypes"]
    data_types = ['book_snapshot_25'] #'trades', 'book_snapshot_5'
    symbol_id = symbol["id"]
    from_date =  symbol["availableSince"]
    #to_date = symbol["availableTo"]
    to_date = '2020-09-30T00:00:00.000Z'

    # skip groupped symbols
    if symbol_id in ['PERPETUALS', 'SPOT', 'FUTURES']:
        continue


    print(f"Downloading {exchange} {data_types} for {symbol_id} from {from_date} to {to_date}")
    datasets.download(
        exchange = exchange,
        data_types = data_types,
        from_date =  from_date,
        to_date = to_date,
        symbols = [symbol_id],
        api_key = "API_KEY",
        download_dir = "./datasets",
    )

    break
