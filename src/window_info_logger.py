########################################################################################################################
#               This file should only contain all code related to logging information regarding app windows.           #
#               Try to keep the code as modular as possible by separating it into functions and classes.               #
#               Code in this file should only be imported into monitorings_software.py.                                #
#               - Keano (03-04-2023)                                                                                   #
#######################################################################################################################

# Library imports here
import win32gui


# Main code here
def active_window_and_title_grabber():
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
    return active_window, window_title


class WindowLogger:
    def __init__(self, file):
        self.active_window = None
        self.active_window_title = None
        self.last_window = None  # Redundant for MVP, but might prove useful in later versions.
        self.last_window_title = None
        self.working_file = file

    def log_window(self):  # This function follows the exact same format as log_clipboard from keystrokes_and_clipboard_logger. Potential for function?
        self.active_window_and_title_grabber()
        if self.active_window_title != self.last_window_title:
            self.working_file.write(f"OPENED {self.active_window_title} \n")
            self.last_window_title = self.active_window_title

    def active_window_and_title_grabber(self):
        """
        Reports back the window that is in focus.
        :return: a tuple containing the active window handle and title
        """
        self.active_window = win32gui.GetForegroundWindow()
        self.active_window_title = win32gui.GetWindowText(self.active_window)

        if self.active_window == 0:
            self.active_window_title = "Desktop"
        elif len(self.active_window_title) == 0:
            self.active_window_title = "Task switching"


def main():
    pass


if __name__ == '__main__':
    main()

