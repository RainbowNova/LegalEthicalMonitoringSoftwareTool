########################################################################################################################
#               Dit is het bestand voor het web en app logger deel.                                                    #
#               Probeer zoveel mogelijk code in functies/classes te plaatsen i.p.v. los.                               #
#               De code in dit bestand wordt geïmporteerd naar monitorings_software.py.                                #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Hier alle library imports
import win32gui


# Hieronder de relevante code
def active_window_grabber(last_active_window):
    """
    Reports back whichever window is in focus in console
    :return: a tuple containing the active window handle and title
    """
    active_window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(active_window)
    if active_window == 0:
        window_title = "Desktop"
    if window_title is not None and window_title != "" and window_title != last_active_window:
        print(window_title)
        return active_window, window_title
    else:
        return active_window, last_active_window


def main():
    pass


if __name__ == '__main__':
    main()

