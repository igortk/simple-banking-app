from typing import Dict

from app.dto.bank_account import BankAccount
from app.dto.user import User


class UsersService:

    def __init__(self):
        self.users: Dict[int, User] = {}

    def register_user(
        self,
        first_name: str,
        last_name: str,
        rntac: int,
        bank_account: BankAccount | None,
    ):
        new_user = (
            User.builder()
            .set_first_name(first_name)
            .set_last_name(last_name)
            .set_rntac(rntac)
            .set_accounts([bank_account])
            .build()
        )

        self.users[rntac] = new_user

        return new_user

    def add_account_for_user(self, rntac: int, account: BankAccount):
        try:
            self.users[rntac].add_account(account)
            return True
        except Exception as ex:
            print(ex)
            return False

    def get_user_by_rntac(self, rntac: int):
        try:
            return self.users[rntac]
        except Exception as ex:
            print(ex)
            return None
