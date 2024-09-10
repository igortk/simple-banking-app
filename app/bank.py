from threading import Lock

from app.services.accounts_service import AccountsService
from app.services.users_service import UsersService


class SingletonMethod(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class Bank(metaclass=SingletonMethod):
    def __init__(self):
        self._users_service = UsersService()
        self._accounts_service = AccountsService()

    def register_new_user(
        self, first_name: str, last_name: str, rntac: int, currency_name: str
    ):
        account = self._accounts_service.register_new_bank_account(
            currency_name
        )
        self._users_service.register_user(
            first_name, last_name, rntac, account
        )

    def add_account_for_user(self, rntac: int, currency_name: str):
        new_account = self._accounts_service.register_new_bank_account(
            currency_name
        )
        self._users_service.add_account_for_user(rntac, new_account)

    def top_up_user_account(self, iban: str, amount: float):
        self._accounts_service.get_account_by_iban(iban).top_up_balance(amount)

    def transfer(self, source_iban: str, destination_iban: str, amount: float):
        self._accounts_service.get_account_by_iban(
            source_iban
        ).write_off_from_balance(amount)
        self._accounts_service.get_account_by_iban(
            destination_iban
        ).top_up_balance(amount)
