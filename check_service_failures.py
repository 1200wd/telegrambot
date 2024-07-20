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


# FIXME: WORK IN PROGRESS....


# Settings
timeout = 10  # seconds
max_failures = 2
message_str_offline = "Oh no, service %s is down"
message_str_online = "Yes, service %s is running again!"
debug = True
hostname = os.uname()[1]


# Monitor and send message
def check_service(service_name):
    service_status = 1 if os.system('systemctl is-active --quiet %s' % service_name) == 0 else 0

    monitor_filename = '.tbot-service-fails-%s' % service_name
    failure_count = file_get_status(monitor_filename)

    if debug:
        print("Failure count: %d" % failure_count)
        print("Current status: %s" % service_status)

    if not service_status and failure_count >= max_failures:
        sendmessage(message_str_offline % service_name + ' (%s)' % hostname)
        file_write_status(monitor_filename, 0)
    elif service_status and not failure_count >= max_failures:
        sendmessage(message_str_online % service_name + ' (%s)' % hostname)
        file_write_status(monitor_filename, 1)


if __name__ == "__main__":
    service_name = sys.argv[1]
    check_service(service_name)
