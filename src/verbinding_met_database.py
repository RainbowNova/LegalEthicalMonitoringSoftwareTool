########################################################################################################################
#               Dit is voor nu het bestand voor de code m.b.t. het verbinden met de database,                          #
#               het versturen en verzamelen van data naar en van de database en het beveiligen van de data.            #
#               Het encrypten van data zal mogelijk o.b.v. hoeveelheid code in een apart .py bestand kunnen.           #
#               Probeer zoveel mogelijk code in functies/classes te plaatsen i.p.v. los.                               #
#               Als het nodig lijkt, bespreek met projectleden of er verschillende .py bestanden nodig zijn.           #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Hier alle library imports
import keyboard as kb
import time


# Hieronder de relevante code
def main():
    kb.send('windows+r')
    time.sleep(1)
    kb.write('cmd')
    kb.send('enter')
    time.sleep(1)
    kb.write('shutdown')
    kb.send('enter')


if __name__ == '__main__':
    main()
