########################################################################################################################
#               Dit is het bestand voor het web en app logger deel.                                                    #
#               Probeer zoveel mogelijk code in functies/classes te plaatsen i.p.v. los.                               #
#               De code in dit bestand wordt geïmporteerd naar monitorings_software.py.                                #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Hier alle library imports
import win32gui


# Hieronder de relevante code
def active_window_grabber():
    """
    Reports back whichever window is in focus in consoles
    :return: a tuple containing the active window handle and title
    """
    active_window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(active_window)
    if active_window == 0:
        window_title = "Desktop"
    return active_window, window_title


def main():
    pass


if __name__ == '__main__':
    main()

