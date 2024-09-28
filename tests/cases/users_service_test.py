import random
from unittest import TestCase

from app.dto.bank_account import BankAccount
from app.services.users_service import UsersService
from app.statics.constants import START_BALANCE_VALUE
from tests.statics.constants import (
    TEST_IBAN,
    DEFAULT_CURRENCY,
    TEST_LAST_NAME,
    TEST_RNTAC,
    TEST_FIRST_NAME,
)


class UsersAccountTest(TestCase):

    def test_register_user(self):
        users_service = UsersService()
        actual_user = users_service.register_user(
            TEST_FIRST_NAME, TEST_LAST_NAME, TEST_RNTAC, None
        )

        expect_user = users_service.get_user_by_rntac(TEST_RNTAC)
        self.assertEqual(actual_user, expect_user)

    def test_add_account_for_user(self):
        rntac = random.randint(1000, 9999)

        users_service = UsersService()
        bank_account = (
            BankAccount.builder()
            .set_iban(TEST_IBAN)
            .set_balance(START_BALANCE_VALUE)
            .set_currency(DEFAULT_CURRENCY)
            .build()
        )
        actual_user = users_service.register_user(
            TEST_FIRST_NAME, TEST_LAST_NAME, rntac, bank_account
        )

        new_bank_account = (
            BankAccount.builder()
            .set_iban(TEST_IBAN + str(random.randint(0, 9)))
            .set_balance(START_BALANCE_VALUE)
            .set_currency(DEFAULT_CURRENCY)
            .build()
        )

        users_service.add_account_for_user(rntac, new_bank_account)

        expected_user = users_service.get_user_by_rntac(rntac)

        self.assertEqual(actual_user, expected_user)

    def test_add_account_for_user_empty_account(self):
        rntac = random.randint(1000, 9999)

        users_service = UsersService()
        result = users_service.add_account_for_user(rntac, None)

        self.assertFalse(result)

    def test_add_account_for_user_empty_rntac(self):
        users_service = UsersService()

        bank_account = (
            BankAccount.builder()
            .set_iban(TEST_IBAN)
            .set_balance(START_BALANCE_VALUE)
            .set_currency(DEFAULT_CURRENCY)
            .build()
        )
        result = users_service.add_account_for_user(None, bank_account)

        self.assertFalse(result)

    def test_get_user_by_rntac_no_present(self):
        users_service = UsersService()
        actual_user = users_service.get_user_by_rntac(
            random.randint(1000, 9999)
        )
        self.assertIsNone(actual_user)
