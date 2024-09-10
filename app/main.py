# This is a sample Python script.
from bank import Bank

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
bank = Bank()
bank2 = Bank()

bank.register_new_user("Art", "tra", 1234, "UAH")
bank.register_new_user("Igr", "rgi", 5364, "UAH")

bank.transfer(
    bank._users_service.users[1234]._accounts[0].iban,
    bank._users_service.users[5364]._accounts[0].iban,
    963,
)
