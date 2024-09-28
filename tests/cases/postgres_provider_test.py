from unittest import TestCase
from unittest.mock import patch

from app.dto.user import User
from app.services import pg_provider
from app.services.pg_provider import PostgresProvider

from tests.statics.constants import TEST_LAST_NAME, TEST_RNTAC, TEST_FIRST_NAME


class PostgresProviderTest(TestCase):
    expect_result = (
        User.builder()
        .set_rntac(TEST_RNTAC)
        .set_last_name(TEST_LAST_NAME)
        .set_first_name(TEST_FIRST_NAME)
        .set_accounts([])
        .build()
    )

    @patch.object(pg_provider.PostgresProvider, "check_connect")
    def test_get_user_by_rntac(self, mock_check):
        mock_check.return_value = True

        actual_result = self.some_test_prepare()

        self.positive_assert_values(actual_result)

    @patch.object(pg_provider.PostgresProvider, "check_connect")
    def test_get_user_by_rntac_false_connect(self, mock_check):
        mock_check.return_value = False
        actual_result = self.some_test_prepare()
        self.assertIsNone(actual_result)

    def some_test_prepare(self):
        provider = PostgresProvider()

        return provider.get_user_by_rntac(TEST_RNTAC)

    def positive_assert_values(self, actual_result):
        self.assertEqual(
            actual_result.get_rntac(), self.expect_result.get_rntac()
        )
        self.assertEqual(
            actual_result.get_first_name(), self.expect_result.get_first_name()
        )
        self.assertEqual(
            actual_result.get_accounts(), self.expect_result.get_accounts()
        )
        self.assertEqual(
            actual_result.get_last_name(), self.expect_result.get_last_name()
        )
