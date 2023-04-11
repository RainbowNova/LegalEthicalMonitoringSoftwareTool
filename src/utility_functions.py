from datetime import datetime
import time


def check_if_time_passed(old_time, time_passed):
    if time.time() - old_time >= time_passed:
        return True


def log_time(text_file, time_since_epoch):
    current_time = datetime.fromtimestamp(time_since_epoch)
    current_time_hour_minute_seconds = current_time.strftime('%H:%M:%S')
    text_file.write(f"\n[TIME]: {current_time_hour_minute_seconds} ")
