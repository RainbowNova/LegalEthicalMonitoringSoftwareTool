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

cursor.execute("CREATE TABLE IF NOT EXISTS application (id INT PRIMARY KEY, name VARCHAR(70))")

