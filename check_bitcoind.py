# Telegram Bot - Server and website monitoring
#
# Check if bitcoind or any other crypto service provider is running
# Uses Python Bitcoinlib
#
# Call from commandline with
# $ python check_bitcoind.py '<bitcoind-url: http://rpcuser:password@server:8332>'
#

import sys
import requests
from hashlib import sha256
from sendmessage import sendmessage
from helpers import file_get_status, file_write_status
from bitcoinlib.services.bitcoind import BitcoindClient


# Settings
timeout = 10  # seconds
message_str_offline = "Oh no, bitcoin node %s seems offline"
message_str_online = "Yes, your bitcoin node %s is online again!"
message_str_blockcount = "Your bitcoin node %s has synced %d blocks"
get_block_count = False
debug = True


# Monitor and send message
def check_bitcoind(bitcoind_url, get_blockcount=False):
    latest_block = None
    try:
        bdc = BitcoindClient(base_url=bitcoind_url)
        latest_block = int(bdc.blockcount())
    except Exception as e:
        if debug:
            print("Error connecting to bitcoind: %s" % str(e))
    monitor_filename = '.tbot-check-bitcoind-' + sha256(bytes(bitcoind_url,'utf8')).hexdigest()
    bitcoind_server = bitcoind_url.split('@')[-1].split(':')[0]
    status_last = file_get_status(monitor_filename)

    if debug:
        print("Last status: %s" % ('Online' if status_last else 'Offline'))
        print("Current blockheight is %s" % latest_block)

    if get_blockcount and latest_block:
        sendmessage(message_str_blockcount % (bitcoind_server, latest_block))
    elif not latest_block and status_last:
        sendmessage(message_str_offline % bitcoind_server)
        file_write_status(monitor_filename, 0)
    elif latest_block and not status_last:
        sendmessage(message_str_online % bitcoind_server)
        file_write_status(monitor_filename, 1)


if __name__ == "__main__":
    bitcoind_url = sys.argv[1]
    get_blockcount = 0 if len(sys.argv) <= 2 else bool(sys.argv[2])
    check_bitcoind(bitcoind_url, get_blockcount)
