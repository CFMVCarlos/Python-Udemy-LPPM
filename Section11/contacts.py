import sqlite3

db: sqlite3.Connection = sqlite3.connect("Section11/contacts.db")

db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute(
    "INSERT INTO contacts (name, phone, email) VALUES ('Carlos', 1234567890, 'carlos@email.com')"
)
db.execute("INSERT INTO contacts VALUES ('Brian', 1234, 'brian@myemail.com')")

cursor: sqlite3.Cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

# for name, phone, email in cursor:
#     print(name, phone, email)

cursor.close()
db.commit()
db.close()
