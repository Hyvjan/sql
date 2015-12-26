# Create a SQLite3 database and table

# import the sqLite3 library
import sqlite3

# Create a new database if the database doesn't already exist
conn=sqlite3.connect("cars.db")


# get cursor 
cursor=conn.cursor()

# create a table
cursor.execute("""CREATE TABLE inventory
	(Make TEXT, Model INT, Quantity INT)
	""")

# close the database connection
conn.close()