# Telegram Bot - Server and website monitoring
#
# Check if systemctl service is running
#
# Call from commandline with
# $ python check_service.py <servicename>
#

import sys
import os
from sendmessage import sendmessage
from helpers import file_get_status, file_write_status


# Settings
timeout = 10  # seconds
message_str_offline = "Oh no, service %s is down"
message_str_online = "Yes, service %s is running again!"
debug = True
hostname = os.uname()[1]


# Monitor and send message
def check_service(service_name):
    service_status = 1 if os.system('systemctl is-active --quiet %s' % service_name) == 0 else 0

    monitor_filename = '.tbot-service-%s' % service_name
    status_last = file_get_status(monitor_filename)

    if debug:
        print("Last status: %s" % ('Online' if status_last else 'Offline'))
        print("Current status: %s" % service_status)

    if not service_status and status_last:
        sendmessage(message_str_offline % service_name + ' (%s)' % hostname)
        file_write_status(monitor_filename, 0)
    elif service_status and not status_last:
        sendmessage(message_str_online % service_name + ' (%s)' % hostname)
        file_write_status(monitor_filename, 1)


if __name__ == "__main__":
    service_name = sys.argv[1]
    check_service(service_name)
