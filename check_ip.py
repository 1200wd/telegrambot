# Check current WAN ip address
#
# Call from commandline with
# $ python check_ip.py
#

import sys
import os
import requests
from sendmessage import sendmessage
from helpers import file_get_status, file_write_status


# Settings
timeout = 10  # seconds
debug = True


# Monitor and send message
def check_ip():
    url = "https://api.ipify.org/"
    try:
        res = requests.get(url, timeout=timeout)
    except Exception as e:
        if debug:
            print("Error connecting to site %s: %s" % (url, str(e)))
        ip_found = False
    else:
        if not 200 <= res.status_code < 400:
            ip_found = False
        else:
            ip_found = res.text

    if debug:
        print(f"WAN ip address is {ip_found}")

    sendmessage(f"WAN ip address is {ip_found}")


if __name__ == "__main__":
    check_ip()
