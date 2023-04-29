# Check date of newest file in directory
# For example to use as basic check if a backup has succeeded

import os
import time
from sendmessage import sendmessage

# Settings
monitor_directory = os.path.expanduser('~')
alarm_after_x_minutes = 2  # Send alarm if newest file is older than x minutes
message_str_offline = "No backups since %d minutes"
message_str_online = "Backups are working again"
debug = True


# Monitor and send message
def get_status():
    try:
        return bool(int(open(monitor_filename, 'r').readline().strip()))
    except Exception:
        pass
    return 1


def write_status(status):
    try:
        open(monitor_filename, 'w').write(str(status))
    except Exception:
        pass


most_recent_time = max([entry.stat().st_mtime for entry in os.scandir(monitor_directory) if entry.is_file()])
latest_update = (time.time()-most_recent_time) // 60
monitor_filename = '.tbot-' + monitor_directory.replace('/', '').replace('\\', '')
status_last = get_status()

if debug:
    print("Last status: %s" % ('Online' if status_last else 'Offline'))
    print("Latest update %d minutes ago" % latest_update)

if latest_update > alarm_after_x_minutes and status_last:
    sendmessage(message_str_offline % latest_update)
    write_status(0)
elif latest_update < alarm_after_x_minutes and not status_last:
    sendmessage(message_str_online)
    write_status(1)

