# ######### Learning Signature #########
#
# Programmed by: Ken Daniel G. Pedrosa
# Date Submitted: September 4, 2026
#
# Program Description: This program generates and saves
# electronic receipts for banking transactions.
#
# Reflection: I learned how to format transaction information
# into a readable electronic receipt and save it to a file.
#
# AI Usage
# [ ] No AI Assistance – Completed independently without AI.
# [X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
#
# ######### Learning Signature #########


from datetime import datetime


def generate_receipt(
    account,
    transaction_type,
    amount,
    balance_after,
    recipient=None
):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    receipt = []
    receipt.append("================================")
    receipt.append("       PEDROSA DIGITAL BANK")
    receipt.append("================================")
    receipt.append(f"Date: {timestamp}")
    receipt.append(f"Account: {account.account_number}")
    receipt.append(f"Name: {account.account_name}")
    receipt.append(f"Transaction: {transaction_type}")
    receipt.append(f"Amount: ₱{amount:,.2f}")

    if recipient:
        receipt.append(f"Recipient: {recipient}")

    receipt.append(f"Balance After: ₱{balance_after:,.2f}")
    receipt.append("================================")
    receipt.append("Thank you for using Pedrosa Digital Bank.")

    return "\n".join(receipt)


def save_receipt(receipt):
    filename = "e_receipt.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(receipt)

    return filename