########################################################################################################################
#            This is the devtool file which contains all code related to obtaining data from the database.             #
#            The resulting testing application functions as proof of the ability to monitor based on collected data.   #
#            Try to keep the code as modular as possible by separating it into functions and classes.                  #
#                                                                                                                      #
#            - Keano (03-04-2023)                                                                                      #
########################################################################################################################

# Library imports here
import tkinter as tk
import pandas as pd


class DataReader:
    def __init__(self, file):
        self.file_from_db = file
        self.edited_file = None

    def read_csv(self, file):
        # Could in theory be replaced with a file search box if it's ever decided to not have a set path like this
        self.file_from_db = pd.read_csv(file, encoding="ISO-8859-1")

    def populate_listbox(self, file, listbox):
        listbox.delete(0, tk.END)
        for index, row in file.iterrows():
            item = f"{row['datetime']} - {row['logged_data']}"
            listbox.insert(tk.END, item)

    def sort_dataframe(self, column):
        self.edited_file = self.file_from_db.sort_values(by=column)

    def filter_dataframe(self, column, value):
        self.edited_file = self.file_from_db[self.file_from_db[column] == value]

    def open_file(self):
        self.read_csv(self.file_from_db)
        self.populate_listbox(self.file_from_db, listbox)

    def sort_by_datetime(self):
        self.sort_dataframe('datetime')
        self.populate_listbox(self.edited_file, listbox)

    def filter_by_error(self, ):
        self.filter_dataframe('severity', 'Error')
        self.populate_listbox(self.edited_file, listbox)


# Main code here


# sets up TKinter environment
root = tk.Tk()
reader = DataReader('logged_data.csv')

# Sets up the buttons
button_frame = tk.Frame(root)
open_button = tk.Button(button_frame, text="Open", command=reader.open_file)
sort_button = tk.Button(button_frame, text="Sort by datetime", command=reader.sort_by_datetime)
filter_button = tk.Button(button_frame, text="Filter by Error", command=reader.filter_by_error)

# Sets up the listbox that will get filled
listbox = tk.Listbox(root)

# Places the buttons and listbox
open_button.pack(side=tk.LEFT)
sort_button.pack(side=tk.LEFT)
filter_button.pack(side=tk.LEFT)

button_frame.pack(side=tk.TOP)
listbox.pack(side=tk.TOP, fill="x", expand=True)

root.mainloop()


def main():
    pass