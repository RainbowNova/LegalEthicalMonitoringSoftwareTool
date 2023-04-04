########################################################################################################################
#               Dit is voor nu het main bestand voor de monitoringssoftware.                                           #
#               Probeer zoveel mogelijk code in functies/classes te plaatsen i.p.v. los.                               #
#               Als het nodig lijkt, bespreek met projectleden of er verschillende .py bestanden nodig zijn.           #
#               - Keano (03-04-2023)                                                                                   #
########################################################################################################################

# Hier alle library imports
import web_and_app_info_logger


# Hieronder de relevante code
def main():

    last_active_window = None
    while True:
        active_window, last_active_window = web_and_app_info_logger.active_window_grabber(last_active_window)


if __name__ == '__main__':
    main()
