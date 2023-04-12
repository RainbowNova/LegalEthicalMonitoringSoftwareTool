import csv

#CREATE DATABASE mydatabase;

#USE mydatabase;

#CREATE TABLE application (
#  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#  applicationname VARCHAR(30) NOT NULL,
#  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#);

import mysql.connector

# Create a new MySQL database connection
conn = mysql.connector.connect(
    host="localhost",
    user="YvoSchutgens",
    password="YpaS-2002",
    database="mydatabase"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

cursor.execute("CREATE TABLE IF NOT EXISTS Main (PCname_id INT PRIMARY KEY, date_and_time datetime,"
               " time VARCHAR(30), window_title VARCHAR(50), logged_data VARCHAR(100), data_id VARCHAR(30))")
cursor.execute("CREATE TABLE IF NOT EXISTS Windows (window_id INT PRIMARY KEY, window_name VARCHAR(30))")
cursor.execute("CREATE TABLE IF NOT EXISTS LoggedData (data_id INT PRIMARY KEY, type_of_data VARCHAR(70))")

with open("logged_data.csv", "r") as file:
    reader = csv.reader(file)
    first_row = next(reader)
    device_name = first_row[0][len("Device name: "):]
    next(reader)  # Date & Time line
    next(reader)  # ===== line
    next(reader)  # Headers line
    for row in reader:
        # datetime,window_title,data_ID,logged_data ==> need to convert window_title to ID! For now auto-increment, but needs to change later because of security issues!
        main_column1 = device_name
        main_column2 = row[0]
        main_column3 = row[1]
        main_column4 = row[3]
        main_column5 = row[2]

        cursor = mydb.cursor()
        # Insert data into Main table, with foreign keys
        cursor.execute(
            "INSERT INTO Windows (window_title) VALUES (%s) ON DUPLICATE KEY UPDATE window_id=LAST_INSERT_ID(window_id)",
            (row[2],))
        window_id = cursor.lastrowid

        # Insert data into LoggedData table
        cursor.execute(
            "INSERT INTO LoggedData (type_of_data) VALUES (%s) ON DUPLICATE KEY UPDATE data_id=LAST_INSERT_ID(data_id)",
            (row[4],))
        data_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO Main (PCname_id, date_and_time, window_id, logged_data, data_id) VALUES (%s, %s, %s, %s, %s)",
            (row[0], row[1], window_id, row[3], data_id))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
