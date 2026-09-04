from datetime import datetime

TRANSACTIONS_FILE = "transactions.txt"


def record_transaction(account, transaction_type, amount):
    # Validate transaction amount
    if amount <= 0:
        return False

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(TRANSACTIONS_FILE, "a", encoding="utf-8") as file:
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Account Number: {account.account_number}\n")
        file.write(f"Account: {account.account_name}\n")
        file.write(f"Account Type: {account.get_account_type()}\n")
        file.write(f"Transaction: {transaction_type}\n")
        file.write(f"Amount: ₱{amount:.2f}\n")
        file.write(f"Balance After: ₱{account.check_balance():.2f}\n")
        file.write("\n")

    return True


def get_transactions():
    transactions = []

    try:
        with open(TRANSACTIONS_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()

        if not content:
            return transactions

        records = content.split("\n\n")

        for record in records:
            lines = record.split("\n")

            if len(lines) < 7:
                continue

            transaction = {
                "timestamp": lines[0].replace("Timestamp: ", ""),
                "account_number": lines[1].replace("Account Number: ", ""),
                "account": lines[2].replace("Account: ", ""),
                "account_type": lines[3].replace("Account Type: ", ""),
                "transaction": lines[4].replace("Transaction: ", ""),
                "amount": lines[5].replace("Amount: ₱", ""),
                "balance_after": lines[6].replace("Balance After: ₱", "")
            }

            transactions.append(transaction)

    except FileNotFoundError:
        return []

    return transactions


"""
######### Learning Signature #########

Programmed by: Ken Daniel G. Pedrosa
Date Submitted: September 4, 2026

Program Description:
This program records and retrieves banking transactions. It stores
transaction details such as the account number, transaction type,
amount, timestamp, and balance after the transaction.

Reflection:
I learned how to use file handling to record transaction history
and retrieve stored transaction data for use in the banking application.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""