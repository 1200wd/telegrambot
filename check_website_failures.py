# Check if website is online
# Open website and check for specific word
#
# Call from commandline with
# $ python check_website.py '<url>' '<expected_word>'
#

import sys
import requests
from sendmessage import sendmessage
from helpers import file_get_count, file_write_count


# Settings
timeout = 10  # seconds
max_failures = 2
reminder_interval = 10
message_str_offline = "Oh no, website %s seems offline"
message_str_offline_reminder = "NOOOO, website %s is still offline. %d failures"
message_str_online = "Yes, website %s is online again!"
debug = True


# Monitor and send message
def check_website(website_url, search_word):
    try:
        res = requests.get(website_url, timeout=timeout)
    except Exception as e:
        if debug:
            print("Error connecting to site %s: %s" % (website_url, str(e)))
        word_found = False
    else:
        if not 200 <= res.status_code < 400:
            word_found = False
        else:
            word_found = search_word in res.text

    website_domain = website_url.split('?')[0]

    monitor_filename = '.tbot-check-website-failures' + \
                       website_domain.replace('/', '').replace('\\', '').replace(':', '').replace('.', '')
    failure_count = file_get_count(monitor_filename)
    if not word_found:
        failure_count += 1
    else:
        failure_count = 0

    if debug:
        print("Failure count: %d" % failure_count)
        print("Word %s found on website %s: %s" % (website_url, search_word, word_found))

    if failure_count == max_failures:
        sendmessage(message_str_offline % website_domain)
    elif failure_count > max_failures and failure_count % reminder_interval == 0:
        sendmessage(message_str_offline_reminder % (website_domain, failure_count))
    elif failure_count < max_failures:
        sendmessage(message_str_online % website_domain)
    file_write_count(monitor_filename, failure_count)


if __name__ == "__main__":
    website_url = sys.argv[1]
    search_word = sys.argv[2]
    check_website(website_url, search_word)
