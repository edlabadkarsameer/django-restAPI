import mysql.connector

# Replace these values with your MySQL server credentials
host = "192.168.30.44"
user = "root"
password = "root"
database = "mydatabase"

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Sample data to insert into the table
data_to_insert = [
    ("John Doe", 25, "john.doe@example.com"),
    ("Jane Smith", 30, "jane.smith@example.com"),
    # Add more data as needed
]

# SQL query to insert data into the table
insert_query = "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)"

# Execute the query for each set of data
for data in data_to_insert:
    cursor.execute(insert_query, data)

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
