########################################################################################################################
#               This file should only contain all code related to logging information regarding app windows.           #
#               Try to keep the code as modular as possible by separating it into functions and classes.               #
#               Code in this file should only be imported into monitorings_software.py.                                #
#               - Keano (03-04-2023)                                                                                   #
#######################################################################################################################

# Library imports here
import win32gui
import getpass


# Main code here
def initialise_log_file(text_file):
    user = getpass.getuser()
    text_file.write(f"User: {user}" + "\n")
    text_file.write("======================================================" + "\n")


def active_window_title_grabber():
    """
    Reports back the window that is in focus.
    :return: a tuple containing the active window handle and title
    """
    active_window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(active_window)
    if active_window == 0:
        window_title = "Desktop"
    elif len(window_title) == 0:
        window_title = "Task switching"
    return window_title


def main():
    pass


if __name__ == '__main__':
    main()

