########################################################################################################################
#            This is the devtool file which contains all code related to obtaining data from the database.             #
#            The resulting testing application functions as proof of the ability to monitor based on collected data.   #
#            Try to keep the code as modular as possible by separating it into functions and classes.                  #
#                                                                                                                      #
#            - Keano (03-04-2023)                                                                                      #
########################################################################################################################

# Library imports here
import tkinter as tk
from tkinter import *
import pandas as pd


class DataReader:
    def __init__(self, file):
        self.file_from_db = file
        self.edited_file = None

    def read_csv(self, file):
        # Could in theory be replaced with a file search box if it's ever decided to not have a set path like this
        self.file_from_db = pd.read_csv(file, encoding="ISO-8859-1", skiprows=3)

    def populate_listbox(self, file, listbox, keyword=None, column=None):
        listbox.delete(0, tk.END)
        for index, row in file.iterrows():
            item = f"{row['datetime']} - {row['window_title']} - {row['data_ID']} - {row['logged_data']}"
            if keyword and column:
                if keyword in str(row[column]):
                    listbox.insert(tk.END, item)
            elif keyword:
                if (keyword in row['datetime'] or
                        keyword in row['window_title'] or
                        keyword in row['data_ID'] or
                        keyword in row['logged_data']):
                    listbox.insert(tk.END, item)
            else:
                listbox.insert(tk.END, item)

    def sort_dataframe(self):
        self.edited_file = self.file_from_db.sort_values(by=var.get())


    def open_file(self):
        self.read_csv(self.file_from_db)
        self.populate_listbox(self.file_from_db, listbox)

    def sort_by_column(self):
        self.sort_dataframe()
        self.populate_listbox(self.edited_file, listbox)

    def search(self):
        keyword = search_box.get()
        column = column_var.get()
        reader.populate_listbox(reader.file_from_db, listbox, keyword, column)


# sets up TKinter environment
root = tk.Tk()
root.title("TROJAN DEVTOOL")
reader = DataReader('logged_data.csv')

# set up sorting and filtering options
options = ["datetime", "window_title", "data_ID"]
var = tk.StringVar(root)
var.set(options[0])

columns = ['datetime', 'window_title', 'data_ID', 'logged_data']
column_var = tk.StringVar(root)
column_var.set(columns[0])

# Sets up the buttons
sort_frame = tk.Frame(root)
search_frame = tk.Frame(root)
search_box = tk.Entry(search_frame)
sort_button = tk.Button(sort_frame, text="Sort", command=reader.sort_by_column)
search_button = tk.Button(search_frame, text="Search", command=reader.search)
reset_button = tk.Button(search_frame, text="Reset", command=reader.open_file)
sorting_dropdown = OptionMenu(sort_frame, var, *options)
column_dropdown = tk.OptionMenu(search_frame, column_var, *columns)

# Sets up the listbox that will get filled
listbox = tk.Listbox(root)

# Places the buttons and listbox
sorting_dropdown.pack(side=tk.LEFT)
sort_button.pack(side=tk.LEFT)
sort_frame.pack(side=tk.TOP)

search_box.pack(side=tk.LEFT)
column_dropdown.pack(side=tk.LEFT)
search_button.pack(side=tk.LEFT)
reset_button.pack(side=tk.LEFT)
search_frame.pack(side=TOP)

listbox.pack(side=tk.BOTTOM, fill="x", expand=True)

reader.open_file()

root.mainloop()


def main():
    pass