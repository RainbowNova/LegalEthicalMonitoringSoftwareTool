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
        self.is_recording = False
        self.events_queue = []
        self.relevant_keys = []

    def start_keylogger_recording(self):
        self.is_recording = True
        kb.start_recording()

    def stop_keylogger_recording(self):
        self.is_recording = False
        previous_events_queue = self.events_queue.copy()
        self.events_queue = kb.stop_recording()
        if len(previous_events_queue) > 0 and isinstance(previous_events_queue, list):
            cut_off_value = len(previous_events_queue)
            print(cut_off_value)
            self.events_queue = self.events_queue[(cut_off_value-1):]
        return self.events_queue

    def get_down_keypresses(self, events_queue):
        # press_events, release_events = self.events_queue
        if len(events_queue) > 0:
            for event in events_queue:
                if event.event_type == 'down':
                    self.relevant_keys.append(event.name)
            return self.relevant_keys


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
