class BankAccount:
    def __init__(self, builder):
        self._iban = builder.iban
        self._balance = builder.balance
        self._currency = builder.currency

    def get_iban(self):
        return self._iban

    def get_balance(self):
        return self._balance

    def get_currency(self):
        return self._currency

    def top_up_balance(self, amount: float):
        self._balance += amount

    def write_off_from_balance(self, amount: float):
        self._balance -= amount

    @staticmethod
    def builder():
        return _BankAccountBuilder()


class _BankAccountBuilder:
    def set_iban(self, iban: str):
        self.iban = iban
        return self

    def set_balance(self, balance: float):
        self.balance = balance
        return self

    def set_currency(self, currency: str):
        self.currency = currency
        return self

    def build(self):
        return BankAccount(self)
