"""
 the property and setter decorators are used to create getter and setter methods for class attributes. They allow you to control the access and modification of attribute values, providing a way to enforce constraints or perform actions when getting or setting a value
"""

class BankAccount:
    def __init__(self, account_holder_name, account_balance=0):
        self._account_holder_name = account_holder_name
        self._account_balance = account_balance

    @property
    def account_holder_name(self):
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Account holder name must be a string")
        self._account_holder_name = value

    @property
    def account_balance(self):
        return self._account_balance

    @account_balance.setter
    def account_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Account balance must be a number")
        if value < 0:
            raise ValueError("Account balance cannot be negative")
        self._account_balance = value


nigeria_account = BankAccount("John Doe", 1000)
print(f"Account Holder Name: {nigeria_account.account_holder_name}")
print(f"Account Balance: {nigeria_account.account_balance}")

nigeria_account.account_holder_name = "Jane Doe"
nigeria_account.account_balance = 1500

print(f"Updated Account Holder Name: {nigeria_account.account_holder_name}")
print(f"Updated Account Balance: {nigeria_account.account_balance}")
