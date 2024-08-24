# Telegram Bot - Server and website monitoring
#
# Check for new Bitcoin transactions for a specific address
# Uses Python Bitcoinlib
#
# Call from commandline with
# $ python check_bitcoin_address.py '<address>'
#

import sys
import requests
from bitcoinlib.wallets import wallet_create_or_open

from sendmessage import sendmessage
from helpers import file_get_status_str, file_write_status
from bitcoinlib.services.services import Service
from bitcoinlib.encoding import *
from bitcoinlib.keys import Address

# Settings
timeout = 10  # seconds
message_str_add_watch = "Start monitoring new transactions for wallet with public masterkey %s"
message_str_new_tx_found = "New transactions for wallet %s with txid %s"
debug = True


# Monitor and send message
def check_wallet(public_masterkey):
    latest_txid = None
    try:
        w = wallet_create_or_open(public_masterkey, public_masterkey)
        w.scan(rescan_used=True)
        txs = w.transactions()
        if txs:
            latest_txid = txs[-1].txid
    except Exception as e:
        if debug:
            print("Error retrieving transactions from server: %s" % str(e))
    monitor_filename = '.tbot-check-wallet-%s' % public_masterkey
    status_last_txid = file_get_status_str(monitor_filename)

    if debug:
        print("Lastest recorded txid / found txid: %s / %s" %
              (status_last_txid if status_last_txid else 'None', latest_txid if latest_txid else 'None'))

    status_last_txid = None if not status_last_txid else status_last_txid
    if status_last_txid != latest_txid:
        if not latest_txid:
            sendmessage(message_str_add_watch % public_masterkey)
        else:
            sendmessage(message_str_new_tx_found % (public_masterkey, latest_txid))
        file_write_status(monitor_filename, "" if not latest_txid else latest_txid)


if __name__ == "__main__":
    public_masterkey = sys.argv[1]
    check_wallet(public_masterkey)
