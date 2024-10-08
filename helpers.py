# Telegram Bot - Server and website monitoring
#
# Helper methods for the Telegrambot methods


def file_get_status(monitor_filename):
    try:
        return bool(int(open(monitor_filename, 'r').readline().strip()))
    except FileNotFoundError:
        pass
    return 1


def file_get_status_str(monitor_filename):
    try:
        return open(monitor_filename, 'r').readline().strip()
    except Exception:
        pass
    return ""


def file_write_status(monitor_filename, status):
    try:
        open(monitor_filename, 'w').write(str(status))
    except Exception:
        pass


def file_get_count(monitor_filename):
    try:
        return int(open(monitor_filename, 'r').readline().strip())
    except Exception:
        pass
    return 1


def file_write_count(monitor_filename, counter):
    try:
        open(monitor_filename, 'w').write(str(counter))
    except Exception:
        pass

