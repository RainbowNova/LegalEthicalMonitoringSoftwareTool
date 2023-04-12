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
    device_name = first_row[3]
    print(device_name)
    next(reader)  # Skip the header row
    for row in reader:
        # Extract the data for each column
        column1 = row[0]
        column2 = int(row[1])
        column3 = row[2]
        column4 = float(row[3])

        # Insert the data into the appropriate MySQL table
        cursor.execute("INSERT INTO table1 (column1, column2) VALUES (%s, %s)", (column1, column2))
        cursor.execute("INSERT INTO table2 (column3, column4) VALUES (%s, %s)", (column3, column4))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()

