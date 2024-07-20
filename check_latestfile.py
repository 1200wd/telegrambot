# Telegram Bot - Server and website monitoring
#
# Check date of newest file in directory
# For example to use as basic check if a backup has succeeded
#
# Call from commandline with
# $ python check_latestfile,py '<directory>' <alarm_after_x_minutes>
#

import os
import sys
import time
from sendmessage import sendmessage
from helpers import file_get_status, file_write_status


# Settings
message_str_offline = "No file changes in directory %s since %d minutes"
message_str_online = "Yes, files in directory %s are updated again!"
debug = True


# Monitor and send message
def check_latestfile(monitor_directory, alarm_after_x_minutes):

    most_recent_time = max([entry.stat().st_mtime for entry in os.scandir(monitor_directory) if entry.is_file()])
    latest_update = (time.time()-most_recent_time) // 60
    monitor_filename = '.tbot-check-latestfile-' + monitor_directory.replace('/', '').replace('\\', '')
    status_last = file_get_status(monitor_filename)

    if debug:
        print("Last status: %s" % ('Online' if status_last else 'Offline'))
        print("Latest update %d minutes ago" % latest_update)

    if latest_update > alarm_after_x_minutes and status_last:
        sendmessage(message_str_offline % (monitor_directory, latest_update))
        file_write_status(monitor_filename, 0)
    elif latest_update < alarm_after_x_minutes and not status_last:
        sendmessage(message_str_online % monitor_directory)
        file_write_status(monitor_filename, 1)


if __name__ == "__main__":
    monitor_directory = sys.argv[1]
    alarm_after_x_minutes = int(sys.argv[2])
    check_latestfile(monitor_directory, alarm_after_x_minutes)
