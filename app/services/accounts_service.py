import random

from app.dto.bank_account import BankAccount
from app.statics.constants import (
    START_BALANCE_VALUE,
    END_INT_RAND,
    START_INT_RAND,
    IBAN_PREFIX,
)


class AccountsService:
    def __init__(self):
        self._accounts = {}

    def register_new_bank_account(self, currency_name: str):
        iban = IBAN_PREFIX + str(random.randint(START_INT_RAND, END_INT_RAND))
        new_account = (
            BankAccount.builder()
            .set_iban(iban)
            .set_currency(currency_name)
            .set_balance(START_BALANCE_VALUE)
            .build()
        )

        self._accounts[iban] = new_account

        return new_account

    def add_users_account(self, bank_account: BankAccount):
        self._accounts[bank_account.get_iban()] = bank_account

    def get_account_by_iban(self, iban: str):
        try:
            return self._accounts[iban]
        except Exception as ex:
            print(ex)
            return None
