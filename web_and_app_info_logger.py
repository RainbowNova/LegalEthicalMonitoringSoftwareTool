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
    Reports back whichever window is in focus in console
    :return:
    """
    last_active_window = None

    
    active_window = win32gui.GetForegroundWindow()
    if active_window != last_active_window:
        last_active_window = active_window
        window_title = win32gui.GetWindowText(active_window)
        if active_window == 0:
            window_title = "Desktop"
        if window_title != "":
            print(f"Active window changed to: {window_title}")


def main():
    active_window_grabber()


if __name__ == '__main__':
    main()

