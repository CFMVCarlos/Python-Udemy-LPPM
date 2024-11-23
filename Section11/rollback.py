import datetime
import sqlite3


class Account:

    @staticmethod
    def _current_time() -> datetime.datetime:
        return datetime.datetime.now(datetime.timezone.utc)

    def __init__(self, name: str, opening_balance: float = 0.0) -> None:
        cursor: sqlite3.Cursor = db.execute(
            "SELECT name, balance FROM accounts WHERE name = ?", (name,)
        )
        row: tuple[str, int] | None = cursor.fetchone()
        if row is not None:
            self.name, self._balance = row
            print(f"Retrieved record for {self.name}. ", end="")
        else:
            self.name: str = name
            self._balance: float = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print(f"Account created for {self.name}. ", end="")
        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._save_update(amount)
            print(f"{amount / 100:.2f} deposited")
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print(f"{amount / 100:.2f} withdrawn")
            return amount / 100
        else:
            print(
                "The amount must be greater than 0 and no more than your account balance"
            )
            return 0.0

    def show_balance(self) -> None:
        print(f"Balance on account {self.name} is {self._balance / 100:.2f}")

    def _save_update(self, amount: int) -> None:
        new_balance: float = self._balance + amount
        withdrawal_time: datetime.datetime = Account._current_time()
        try:
            db.execute(
                "UPDATE accounts SET balance = ? WHERE name = ?",
                (new_balance, self.name),
            )
            db.execute(
                "INSERT INTO transactions (time, account, amount) VALUES(?, ?, ?)",
                (withdrawal_time, self.name, amount),
            )
        except sqlite3.Error:
            db.rollback()
        else:
            db.commit()
            self._balance = new_balance


def main() -> None:
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("Terry")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)

    db.close()


if __name__ == "__main__":
    db: sqlite3.Connection = sqlite3.connect("Section11/accounts.db")
    db.execute(
        "CREATE TABLE IF NOT EXISTS accounts (\            name TEXT PRIMARY KEY NOT NULL, \
                balance INTEGER NOT NULL)"
    )
    db.execute(
        "CREATE TABLE IF NOT EXISTS transactions (\
            time TIMESTAMP NOT NULL, \
            account TEXT NOT NULL, \
            amount INTEGER NOT NULL, \
            PRIMARY  KEY (time, account))"
    )
    db.execute(
        "CREATE VIEW IF NOT EXISTS local_transactions AS \
            SELECT strftime('%Y-%m-%d %H:%M:%f', transactions.time, 'localtime') AS localtime, \
            transactions.account, transactions.amount FROM transactions \
            ORDER BY transactions.time"
    )

    main()
