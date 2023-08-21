import sqlite3


#connect to database
conn = sqlite3.connect('database.db')

#create a cursor object to execute SQL quaries
cursor = conn.cursor()

#Execute a SQL quary
cursor.execute('SELECT * FROM users')

#Fetch all results
results = cursor.fetchall()

#print the results
for row in results:
    print(row)
    
    #Close the cursor and connection
    cursor.close()
    conn.close()
