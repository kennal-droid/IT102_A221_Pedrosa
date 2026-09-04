"""
######### Learning Signature #########

Programmed by: Ken Daniel G. Pedrosa
Date Submitted: September 4, 2026

Program Description: This program analyzes ATM transaction records
and calculates transaction statistics such as deposits, withdrawals,
totals, averages, and the latest transaction.

Reflection: I learned how to process transaction records from a file,
store them in dictionaries and lists, and calculate useful statistics.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

def analyze_transactions():

    # TODO 1
    try:
        with open("transactions.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

    # TODO 2
    except FileNotFoundError:
        return {
            "total_transactions": 0,
            "deposits": 0,
            "withdrawals": 0,
            "total_deposited": 0.0,
            "total_withdrawn": 0.0,
            "average_transaction": 0.0,
            "latest_transaction": None,
            "latest_timestamp": None,
            "largest_transaction": 0.0
        }

    # TODO 3
    transactions = []

    # TODO 4
    current = {}

    # TODO 5
    for line in lines:

        # TODO 6
        line = line.strip()

        # TODO 7
        if not line:
            continue

        # TODO 8
        if line.startswith("Timestamp:"):
            current["timestamp"] = line.replace("Timestamp:", "").strip()

        # TODO 9
        elif line.startswith("Account:"):
            current["account"] = line.replace("Account:", "").strip()

        # TODO 10
        elif line.startswith("Transaction:"):
            current["transaction"] = line.replace("Transaction:", "").strip()

        # TODO 11
        elif line.startswith("Amount:"):
            amount_text = line.replace("Amount:", "").strip()
            amount_text = amount_text.replace("₱", "").replace(",", "")
            current["amount"] = float(amount_text)

            # TODO 12
            if (
                "timestamp" in current
                and "account" in current
                and "transaction" in current
                and "amount" in current
            ):
                transactions.append(current)
                current = {}

    # TODO 13
    total_transactions = len(transactions)

    # TODO 14
    deposits = sum(
        1 for transaction in transactions
        if transaction["transaction"] == "Deposit"
    )

    # TODO 15
    withdrawals = sum(
        1 for transaction in transactions
        if transaction["transaction"] == "Withdraw"
    )

    # TODO 16
    total_deposited = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["transaction"] == "Deposit"
    )

    # TODO 17
    total_withdrawn = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["transaction"] == "Withdraw"
    )

    # TODO 18
    if transactions:
        largest_transaction = max(
            transaction["amount"]
            for transaction in transactions
        )
    else:
        largest_transaction = 0.0

    # TODO 19 and TODO 20
    if transactions:
        latest = max(
            transactions,
            key=lambda transaction: transaction["timestamp"]
        )

        latest_transaction = latest["transaction"]
        latest_timestamp = latest["timestamp"]

    else:
        latest_transaction = None
        latest_timestamp = None

    # TODO 21
    if total_transactions > 0:
        average_transaction = (
            sum(transaction["amount"] for transaction in transactions)
            / total_transactions
        )
    else:
        average_transaction = 0.0

    # TODO 22
    return {
        "total_transactions": total_transactions,
        "deposits": deposits,
        "withdrawals": withdrawals,
        "total_deposited": total_deposited,
        "total_withdrawn": total_withdrawn,
        "average_transaction": average_transaction,
        "latest_transaction": latest_transaction,
        "latest_timestamp": latest_timestamp,
        "largest_transaction": largest_transaction
    }