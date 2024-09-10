from app.dto.bank_account import BankAccount


class User:
    def __init__(self, builder):
        self._first_name = builder.first_name
        self._last_name = builder.last_name
        self._rntac = builder.rntac
        self._accounts = builder.accounts

    def get_rntac(self):
        return self._rntac

    def get_last_name(self):
        return self._last_name

    def get_first_name(self):
        return self._first_name

    def get_accounts(self):
        return self._accounts

    def add_account(self, account: BankAccount):
        self._accounts.append(account)

    @staticmethod
    def builder():
        return _UserBuilder()


class _UserBuilder:
    def set_first_name(self, first_name: str):
        self.first_name = first_name
        return self

    def set_last_name(self, last_name: str):
        self.last_name = last_name
        return self

    def set_accounts(self, accounts: [BankAccount]):
        self.accounts = accounts
        return self

    def set_rntac(self, rntac: int):
        self.rntac = rntac
        return self

    def build(self):
        return User(self)
