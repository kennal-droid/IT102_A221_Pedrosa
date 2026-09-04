from Pedrosa_bank_account import SavingsAccount, StudentAccount

USERS_FILE = "users.txt"


def save_account(account):
    with open(USERS_FILE, "a", encoding="utf-8") as file:
        file.write(f"Account Number: {account.account_number}\n")
        file.write(f"Account Name: {account.account_name}\n")
        file.write(f"PIN: {account.get_pin()}\n")
        file.write(f"Account Type: {account.get_account_type()}\n")
        file.write(f"Balance: {account.check_balance():.2f}\n")

        if account.savings_goal:
            file.write(f"Savings Goal: {account.savings_goal}\n")
            file.write(f"Savings Target: {account.savings_target:.2f}\n")

        file.write("\n")


def load_accounts():
    accounts = []

    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()

        if not content:
            return accounts

        records = content.split("\n\n")

        for record in records:
            lines = record.split("\n")

            if len(lines) < 5:
                continue

            account_number = lines[0].replace("Account Number: ", "")
            name = lines[1].replace("Account Name: ", "")
            pin = lines[2].replace("PIN: ", "")
            account_type = lines[3].replace("Account Type: ", "")
            balance = float(lines[4].replace("Balance: ", ""))

            if account_type == "Savings Account":
                account = SavingsAccount(
                    account_number,
                    name,
                    pin,
                    balance
                )

            elif account_type == "Student Account":
                account = StudentAccount(
                    account_number,
                    name,
                    pin,
                    balance
                )

            else:
                continue

            for line in lines[5:]:
                if line.startswith("Savings Goal: "):
                    account.savings_goal = line.replace(
                        "Savings Goal: ",
                        ""
                    )

                elif line.startswith("Savings Target: "):
                    account.savings_target = float(
                        line.replace("Savings Target: ", "")
                    )

            accounts.append(account)

    except FileNotFoundError:
        return []

    return accounts


def account_exists(account_number):
    accounts = load_accounts()

    for account in accounts:
        if account.account_number == account_number:
            return True

    return False


def find_account(account_number):
    accounts = load_accounts()

    for account in accounts:
        if account.account_number == account_number:
            return account

    return None


def update_account(account):
    accounts = load_accounts()

    with open(USERS_FILE, "w", encoding="utf-8") as file:

        for saved_account in accounts:

            if saved_account.account_number == account.account_number:
                saved_account.set_balance(
                    account.check_balance()
                )

                saved_account._pin = account.get_pin()

                saved_account.savings_goal = account.savings_goal
                saved_account.savings_target = account.savings_target

            file.write(
                f"Account Number: {saved_account.account_number}\n"
            )

            file.write(
                f"Account Name: {saved_account.account_name}\n"
            )

            file.write(
                f"PIN: {saved_account.get_pin()}\n"
            )

            file.write(
                f"Account Type: {saved_account.get_account_type()}\n"
            )

            file.write(
                f"Balance: {saved_account.check_balance():.2f}\n"
            )

            if saved_account.savings_goal:
                file.write(
                    f"Savings Goal: {saved_account.savings_goal}\n"
                )

                file.write(
                    f"Savings Target: "
                    f"{saved_account.savings_target:.2f}\n"
                )

            file.write("\n")



"""
######### Learning Signature #########

Programmed by: Ken Daniel G. Pedrosa
Date Submitted: September 4, 2026

Program Description:
This program handles saving, loading, searching, and updating bank
account information using the users.txt file.

Reflection:
I learned how to use file handling in Python to store and retrieve
account information and how to connect stored data with bank account
objects.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""