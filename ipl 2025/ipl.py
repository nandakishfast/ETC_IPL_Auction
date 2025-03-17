import sqlite3

# Connect to the SQLite database (if it doesn't exist, a new database will be created)
conn = sqlite3.connect('ipl2.db')

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Create a table
cur.execute('''CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY autoincrement,
                name TEXT NOT NULL,
                country TEXT,
                type TEXT
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS buys (
                player_id INTEGER PRIMARY KEY,
                price INTEGER,
                team TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')

with open('players data.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Print each line (remove trailing newline character)
        ln = line.strip().split('	')
        # Insert data into the table
        country = ln[1]
        player = ln[0]
        type_ = ln[2]
        cur.execute("INSERT INTO players (name, country, type) VALUES (?, ?, ?)", (player,country, type_))


# Commit the transaction
conn.commit()

# Close the connection
conn.close()