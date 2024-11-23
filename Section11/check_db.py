import datetime
import sqlite3

db: sqlite3.Connection = sqlite3.connect(
    "Section11/accounts.db", detect_types=sqlite3.PARSE_DECLTYPES
)

for row in db.execute("SELECT * FROM accounts"):
    print(row)

print("*" * 80)

for row in db.execute("SELECT * FROM transactions"):
    # print(row)
    utc_time = row[0].replace(tzinfo=datetime.timezone.utc)
    local_time = utc_time.astimezone()
    print(f"{utc_time}\t{local_time}")

print("*" * 80)

for row in db.execute(
    "SELECT strftime('%Y-%m-%d %H:%M:%f', transactions.time, 'localtime') AS localtime, \
        transactions.account, transactions.amount FROM transactions \
        ORDER BY transactions.time"
):
    print(row)

print("*" * 80)

for row in db.execute("SELECT * FROM local_transactions"):
    print(row)

db.close()
