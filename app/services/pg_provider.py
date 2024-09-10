import random

from app.dto.user import User


class PostgresProvider:

    def get_user_by_rntac(self, rntac: int):
        if self.check_connect():
            return (
                User.builder()
                .set_rntac(rntac)
                .set_last_name("FIRST_NAME")
                .set_first_name("FIRST_NAME")
                .set_accounts([])
                .build()
            )

        return None

    def check_connect(self):
        return random.randint(0, 1)
