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

cursor.execute("CREATE TABLE IF NOT EXISTS Main (PCname_id INT PRIMARY KEY, date VARCHAR(30), time VARCHAR(30), window_title VARCHAR(50), logged_data VARCHAR(100), data_id VARCHAR(30))")
cursor.execute("CREATE TABLE IF NOT EXISTS Applications (application_id INT PRIMARY KEY, application_name VARCHAR(30))")
cursor.execute("CREATE TABLE IF NOT EXISTS Windows (window_id INT PRIMARY KEY, window_name VARCHAR(30))")
cursor.execute("CREATE TABLE IF NOT EXISTS LoggedData (data_id INT PRIMARY KEY, type_of_data VARCHAR(70))")

