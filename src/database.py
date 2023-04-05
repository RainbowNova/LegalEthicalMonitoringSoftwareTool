#CREATE DATABASE mydatabase;

#USE mydatabase;

#CREATE TABLE application (
#  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#  applicationname VARCHAR(30) NOT NULL,
#  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#);

import mysql.connector

# Create a new MySQL database connection
db = mysql.connector.connect(
    host="TROJAN",
    user="TROJAN",
    password="de mam"
)

# Create a new database
cursor = db.cursor()
cursor.execute("CREATE DATABASE mydatabase")

# Switch to the new database
cursor.execute("USE mydatabase")

# Create a new table
cursor.execute("CREATE TABLE application (id INT(11) NOT NULL AUTO_INCREMENT, ApplicationName VARCHAR(255) NOT NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id))")

# Insert some sample data
cursor.execute("INSERT INTO users (ApplicationName) VALUES ('Discord')")
cursor.execute("INSERT INTO users (ApplicationName) VALUES ('Word')")

# Commit the changes to the database
db.commit()

# Close the database connection
db.close()
