import sqlite3

# Create a new SQLite database
conn = sqlite3.connect('instance/data.db')
# Close the database connection
conn.close()
