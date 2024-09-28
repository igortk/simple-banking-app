from unittest import TestCase, main

from app.bank import Bank


class BankTest(TestCase):
    def test_singleton(self):
        first_bank = Bank()
        second_bank = Bank()

        self.assertEqual(first_bank, second_bank)
