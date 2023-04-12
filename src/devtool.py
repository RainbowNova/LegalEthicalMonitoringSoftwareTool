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


# Main code here
def read_csv():
    # Could in theory be replaced with a file search box if it's ever decided to not have a set path like this
    df = pd.read_csv('logged_data.csv', encoding="ISO-8859-1")
    return df


def populate_listbox(df, listbox):
    listbox.delete(0, tk.END)
    for index, row in df.iterrows():
        item = f"{row['datetime']} - {row['logged_data']}"
        listbox.insert(tk.END, item)


def sort_dataframe(df, column):
    df_sorted = df.sort_values(by=column)
    return df_sorted


def filter_dataframe(df, column, value):
    df_filtered = df[df[column] == value]
    return df_filtered


def open_file():
    df = read_csv()
    populate_listbox(df, listbox)


def sort_by_datetime():
    df_sorted = sort_dataframe(df, 'datetime')
    populate_listbox(df_sorted, listbox)


def filter_by_error():
    df_filtered = filter_dataframe(df, 'severity', 'Error')
    populate_listbox(df_filtered, listbox)


# sets up TKinter environment
root = tk.Tk()

# Sets up the buttons
button_frame = tk.Frame(root)
open_button = tk.Button(button_frame, text="Open", command=open_file)
sort_button = tk.Button(button_frame, text="Sort by datetime", command=sort_by_datetime)
filter_button = tk.Button(button_frame, text="Filter by Error", command=filter_by_error)

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


if __name__ == '__main__':
    main()
