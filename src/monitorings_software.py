########################################################################################################################
#               Dit is voor nu het main bestand voor de monitoringssoftware.                                           #
#               Probeer zoveel mogelijk code in functies/classes te plaatsen i.p.v. los.                               #
#               Als het nodig lijkt, bespreek met projectleden of er verschillende .py bestanden nodig zijn.           #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Hier alle library imports
import web_and_app_info_logger
import os
import datetime


# Hieronder de relevante code
def main():
    if os.path.isfile("keyboard_events.txt"):
        # Code voor versturen van het bestand naar DB
        print("Bestand is verstuurd naar de database!")
    with open("keyboard_events.txt", 'w') as f:
        last_active_window = None
        while True:
            active_window, active_window_title = web_and_app_info_logger.active_window_grabber()
            if active_window != last_active_window and active_window_title != "":
                f.write("OPENED " + active_window_title + " AT TIME " + str(datetime.datetime.now()) + "\n")
            last_active_window = active_window

    # Begin van programma, maak txt file o.b.v. datum + tijdstip
    # Zolang programma runned, controleer welke applicatie openstaat.
    # Als nieuwe applicatie geopend, schrijf op nieuwe regel "OPENED {applicatienaam} met misschien tijd + datum erbij"
    # Alle gelogde keys onder die regel ==> elk karakter nieuwe regel? Elk woord? 1 lange string?
    # Als applicatie gesloten ==> noteer in tekstbestand met tijdstip? (Nodig?)
    # Als applicatie niet gesloten ==> niks doen.



if __name__ == '__main__':
    main()