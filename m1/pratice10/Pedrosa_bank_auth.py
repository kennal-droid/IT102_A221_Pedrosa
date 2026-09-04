from Pedrosa_bank_account import SavingsAccount, StudentAccount
import Pedrosa_bank_storage


def validate_pin(pin):
    pin = pin.strip()

    if len(pin) != 4:
        return False

    if not pin.isdigit():
        return False

    return True


def register_account(account_number, name, pin, confirm_pin,
                     account_type, starting_balance):

    if not name.strip():
        return None, "Account name cannot be empty."

    if not account_number.strip():
        return None, "Account number cannot be empty."

    if Pedrosa_bank_storage.account_exists(account_number):
        return None, "Account number already exists."

    if not validate_pin(pin):
        return None, "PIN must be exactly 4 digits."

    if pin != confirm_pin:
        return None, "PINs do not match."

    if starting_balance < 0:
        return None, "Starting balance cannot be negative."

    if account_type == "Savings Account":
        account = SavingsAccount(
            account_number,
            name,
            pin,
            starting_balance
        )

    elif account_type == "Student Account":
        account = StudentAccount(
            account_number,
            name,
            pin,
            starting_balance
        )

    else:
        return None, "Invalid account type."

    Pedrosa_bank_storage.save_account(account)

    return account, "Registration successful."


def login_account(account_number, pin):

    account = Pedrosa_bank_storage.find_account(account_number)

    if account is None:
        return None, "Account not found."

    if not account.verify_pin(pin):
        return None, "Incorrect PIN."

    return account, "Login successful."



"""
######### Learning Signature #########

Programmed by: Ken Daniel G. Pedrosa
Date Submitted: September 4, 2026

Program Description:
This program handles user registration and login for the banking
application. It validates account information and PINs and creates
the appropriate bank account type.

Reflection:
I learned how to validate user input, handle account registration
and login, and connect authentication functions with the banking
account and storage modules.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""