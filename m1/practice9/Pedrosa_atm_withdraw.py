"""
######### Learning Signature #########

Programmed by: Ken Daniel G. Pedrosa
Date Submitted: September 4, 2026

Program Description: This program processes ATM withdrawals,
updates the Account object, and records successful transactions.

Reflection: I learned how to use an Account object to validate
withdrawals and record successful transactions.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

from datetime import datetime


def withdraw_money(account, amount):

    # TODO 3: Reject zero or negative amounts
    if amount <= 0:
        return False

    # TODO 4: Call Account object's withdraw()
    result = account.withdraw(amount)

    # TODO 5: Create timestamp if successful
    if result:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # TODO 6: Open transactions.txt using append mode
        with open("transactions.txt", "a", encoding="utf-8") as file:

            # TODO 7: Write timestamp
            file.write(f"Timestamp: {timestamp}\n")

            # TODO 8: Write account name
            file.write(f"Account: {account.account_name}\n")

            # TODO 9: Write transaction type
            file.write("Transaction: Withdraw\n")

            # TODO 10: Write withdrawal amount
            file.write(f"Amount: ₱{amount:.2f}\n")

            file.write("\n")

        # TODO 11: Successful withdrawal
        return True

    # TODO 12: Failed withdrawal
    return False