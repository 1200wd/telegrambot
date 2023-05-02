# Check if website is online
# Open website and check for specific word
#
# Call from commandline with
# $ python check_website.py '<url>' '<expected_word>'
#

import sys
import requests
from sendmessage import sendmessage
from helpers import file_get_status, file_write_status


# Settings
message_str_offline = "Oh no, website %s seems offline"
message_str_online = "Yes, website %s is online again!"
debug = True


# Monitor and send message
def check_website(website_url, search_word):
    res = requests.get(website_url)
    if not 200 <= res.status_code < 400:
        word_found = False
    else:
        word_found = search_word in res.text

    monitor_filename = '.tbot-check-website-' + \
                       website_url.replace('/', '').replace('\\', '').replace(':', '').replace('.', '')
    status_last = file_get_status(monitor_filename)

    if debug:
        print("Last status: %s" % ('Online' if status_last else 'Offline'))
        print("Word %s found on website %s: %s" % (website_url, search_word, word_found))

    if not word_found and status_last:
        sendmessage(message_str_offline % (website_url))
        file_write_status(monitor_filename, 0)
    elif word_found and not status_last:
        sendmessage(message_str_online % website_url)
        file_write_status(monitor_filename, 1)


if __name__ == "__main__":
    website_url = sys.argv[1]
    search_word = sys.argv[2]
    check_website(website_url, search_word)
