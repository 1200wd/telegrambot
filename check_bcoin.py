# Telegram Bot - Server and website monitoring
#
# Check if Bcoin or any other crypto service provider is running
# Uses Python Bitcoinlib
#
# Call from commandline with
# $ python check_bcoin.py '<bcoin-url: http://user:password@server:port>'
#

import sys
import requests
from hashlib import sha256
from sendmessage import sendmessage
from helpers import file_get_status, file_write_status
from bitcoinlib.services.bcoin import BcoinClient


# Settings
timeout = 10  # seconds
message_str_offline = "Oh no, Bcoin node %s seems offline"
message_str_online = "Yes, your Bcoin node %s is online again!"
message_str_blockcount = "Your Bcoin node %s has synced %d blocks"
get_block_count = False
debug = True


# Monitor and send message
def check_bcoin(bcoin_url, get_blockcount=False):
    latest_block = None
    try:
        bdc = BcoinClient(base_url=bcoin_url, network='testnet', denominator=100000000)
        latest_block = int(bdc.blockcount())
    except Exception as e:
        if debug:
            print("Error connecting to Bcoin: %s" % str(e))
    monitor_filename = '.tbot-check-bcoin-' + sha256(bytes(bcoin_url,'utf8')).hexdigest()
    bcoin_server = bcoin_url.split('@')[-1].split(':')[0]
    status_last = file_get_status(monitor_filename)

    if debug:
        print("Last status: %s" % ('Online' if status_last else 'Offline'))
        print("Current blockheight is %s" % latest_block)

    if get_blockcount and latest_block:
        sendmessage(message_str_blockcount % (bcoin_server, latest_block))
    elif not latest_block and status_last:
        sendmessage(message_str_offline % bcoin_server)
        file_write_status(monitor_filename, 0)
    elif latest_block and not status_last:
        sendmessage(message_str_online % bcoin_server)
        file_write_status(monitor_filename, 1)


if __name__ == "__main__":
    bcoin_url = sys.argv[1]
    get_blockcount = 0 if len(sys.argv) <= 2 else bool(sys.argv[2])
    check_bcoin(bcoin_url, get_blockcount)
