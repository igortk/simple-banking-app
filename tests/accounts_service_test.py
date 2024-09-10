import random
import re
from unittest import TestCase
from unittest.mock import patch

from app.dto.bank_account import BankAccount
from app.services.accounts_service import AccountsService
from app.statics.constants import (
    START_BALANCE_VALUE,
    IBAN_PREFIX,
    END_INT_RAND,
    START_INT_RAND,
)
from tests.statics.constants import DEFAULT_CURRENCY, TEST_IBAN


class AccountServiceTest(TestCase):
    account_service = AccountsService()
    expect_result = (
        BankAccount.builder()
        .set_iban(IBAN_PREFIX)
        .set_currency(DEFAULT_CURRENCY)
        .set_balance(START_BALANCE_VALUE)
        .build()
    )

    def test_register_new_bank_account(self):
        regex_iban = f"^{IBAN_PREFIX}"

        actual_result = self.account_service.register_new_bank_account(
            DEFAULT_CURRENCY
        )

        self.assertEqual(
            actual_result.get_currency(), self.expect_result.get_currency()
        )
        self.assertEqual(
            actual_result.get_balance(), self.expect_result.get_balance()
        )
        self.assertTrue(re.match(regex_iban, actual_result.get_iban()))

    def test_add_user_account(self):
        iban = IBAN_PREFIX + str(random.randint(START_INT_RAND, END_INT_RAND))

        account = (
            BankAccount.builder()
            .set_iban(iban)
            .set_balance(START_BALANCE_VALUE)
            .set_currency(DEFAULT_CURRENCY)
            .build()
        )
        self.account_service.add_users_account(account)

        result = self.account_service.get_account_by_iban(iban)

        self.assertEqual(result, account)

    def test_get_account_by_iban(self):
        account_service = AccountsService()
        result = account_service.get_account_by_iban(TEST_IBAN)
        self.assertIsNone(result)
