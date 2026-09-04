from datetime import datetime


def deposit_money(account, amount):

    # TODO 3: Validate amount
    if amount <= 0:
        return False

    # TODO 4: Ask Account object to perform deposit
    result = account.deposit(amount)

    # TODO 5: Create timestamp if successful
    if result:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # TODO 6: Open transactions.txt in append mode
        with open("transactions.txt", "a", encoding="utf-8") as file:

            # TODO 7: Write timestamp
            file.write(f"Timestamp: {timestamp}\n")

            # TODO 8: Write account name
            file.write(f"Account: {account.account_name}\n")

            # TODO 9: Write transaction type
            file.write("Transaction: Deposit\n")

            # TODO 10: Write amount
            file.write(f"Amount: ₱{amount:.2f}\n")

            file.write("\n")

        # TODO 11: Successful
        return True

    # TODO 12: Unsuccessful
    return False


"""
######### Learning Signature #########

Programmed by: Ken Daniel G. Pedrosa
Date Submitted: September 4, 2026

Program Description: This program processes ATM deposits,
updates the Account object, and records successful transactions.

Reflection: I learned how to connect a deposit module with an
Account object and record transactions in a text file.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""