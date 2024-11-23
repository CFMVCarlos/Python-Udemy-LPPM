from datetime import datetime, timezone


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time() -> str:
        return datetime.now(timezone.utc).astimezone().isoformat()

    def __init__(self, name: str, balance: float) -> None:
        self._name: str = name
        #! This makes python do name mangling, so the attribute is not directly accessible
        #! This is not a security feature, it is just to avoid name clashes
        #! The attribute is still accessible as _Account__balance
        self.__balance: float = balance
        self._transaction_list: list[tuple[str, float]] = [
            (Account._current_time(), self.__balance)
        ]
        print(f"Account created for {self._name}")

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print(
                "The amount must be greater than 0 and no more than your account balance"
            )
        self.show_balance()

    def show_balance(self) -> None:
        print(f"Balance: {self.__balance}")

    def show_transactions(self) -> None:
        for date, amount in self._transaction_list:
            if amount >= 0:
                tran_type: str = "deposited"
            else:
                tran_type: str = "withdrawn"
                amount *= -1
            print(f"{amount:6} {tran_type} on {date}")


def main():
    account: Account = Account("Darragh", 0)
    # Next line will not work because __balance is a private attribute where the name is mangled
    # account.__balance = 200
    account._Account__balance = 200
    account.deposit(1000)
    account.withdraw(500)
    account.withdraw(2000)
    account.deposit(500)
    account.withdraw(2000)

    account.show_transactions()
    account.show_balance()


if __name__ == "__main__":
    main()
