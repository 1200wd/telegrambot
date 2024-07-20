# Check if server is online
#
# Call from commandline with
# $ python check_website.py '<url>' '<expected_word>'
#

import sys
import os
from sendmessage import sendmessage
from helpers import file_get_status, file_write_status


# Settings
timeout = 10  # seconds
message_str_offline = "Oh no, server %s seems offline"
message_str_online = "Yes, server %s is online again!"
debug = True


# Monitor and send message
def check_ping(hostname):
    try:
        res = os.system("ping -c 1 " + hostname)
    except Exception as e:
        if debug:
            print("Error pinging host %s: %s" % (hostname, str(e)))
        ping_result = False
    else:
        ping_result = True if res == 0 else False

    monitor_filename = '.tbot-ping-' + \
                       hostname.replace('/', '_').replace('\\', '_').replace(':', '_').replace('.', '_')
    status_last = file_get_status(monitor_filename)

    if debug:
        print("Last status: %s" % ('Online' if status_last else 'Offline'))
        print("Ping result %s: %s" % (hostname, ping_result))

    if not ping_result and status_last:
        sendmessage(message_str_offline % hostname)
        file_write_status(monitor_filename, 0)
    elif ping_result and not status_last:
        sendmessage(message_str_online % hostname)
        file_write_status(monitor_filename, 1)


if __name__ == "__main__":
    hostname = sys.argv[1]
    check_ping(hostname)
