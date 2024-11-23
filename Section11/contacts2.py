import sqlite3

# SQL injection attack example
# The attacker can input a phone number along with sql code to delete the entire table

db: sqlite3.Connection = sqlite3.connect("Section11/contacts.db")

new_email: str = "new_email@update.com"
phone: str = input("Please enter the phone number: ")
# phone: int = 1234

# update_sql: str = (
#     f"UPDATE contacts SET email = '{new_email}' WHERE contacts.phone = {phone}"
# )
update_sql: str = f"UPDATE contacts SET email = ? WHERE contacts.phone = ?"
update_cursor: sqlite3.Cursor = db.cursor()
#! Dangerous because it allows for SQL injection attacks
# update_cursor.executescript(update_sql)
update_cursor.execute(update_sql, (new_email, phone))
print(f"{update_cursor.rowcount} rows updated")
update_cursor.connection.commit()
update_cursor.close()

for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()
