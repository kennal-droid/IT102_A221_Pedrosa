def analyze_transactions(transactions):
    total_transactions = len(transactions)

    deposits = 0
    withdrawals = 0
    total_deposited = 0
    total_withdrawn = 0

    largest_transaction = 0
    average_transaction = 0
    latest_transaction = None
    latest_timestamp = ""

    for transaction in transactions:
        amount = float(transaction["amount"])

        if transaction["transaction"] == "Deposit":
            deposits += 1
            total_deposited += amount

        elif transaction["transaction"] == "Withdraw":
            withdrawals += 1
            total_withdrawn += amount

        if amount > largest_transaction:
            largest_transaction = amount

        if transaction["timestamp"] > latest_timestamp:
            latest_timestamp = transaction["timestamp"]
            latest_transaction = transaction

    if total_transactions > 0:
        average_transaction = (
            total_deposited + total_withdrawn
        ) / total_transactions

    net_cash_flow = total_deposited - total_withdrawn

    deposit_ratio = 0
    withdrawal_ratio = 0

    if total_transactions > 0:
        deposit_ratio = (deposits / total_transactions) * 100
        withdrawal_ratio = (withdrawals / total_transactions) * 100

    return {
        "total_transactions": total_transactions,
        "deposits": deposits,
        "withdrawals": withdrawals,
        "total_deposited": total_deposited,
        "total_withdrawn": total_withdrawn,
        "net_cash_flow": net_cash_flow,
        "largest_transaction": largest_transaction,
        "average_transaction": average_transaction,
        "latest_transaction": latest_transaction,
        "deposit_ratio": deposit_ratio,
        "withdrawal_ratio": withdrawal_ratio
    }

"""
######### Learning Signature #########

Programmed by: Ken Daniel G. Pedrosa
Date Submitted: September 4, 2026

Program Description:
This program analyzes banking transactions by calculating the total number
of transactions, deposits, withdrawals, total amounts, net cash flow,
largest transaction, average transaction, and latest transaction.

Reflection:
I learned how to process transaction data in Python and use functions
to calculate useful financial information from banking records.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""