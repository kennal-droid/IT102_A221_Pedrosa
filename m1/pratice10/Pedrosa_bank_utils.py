def is_valid_amount(amount):
    return amount > 0


def format_currency(amount):
    return f"₱{amount:,.2f}"


def format_transaction_count(count):
    if count == 1:
        return "1 transaction"

    return f"{count} transactions"



"""
######### Learning Signature #########

Programmed by: Ken Daniel G. Pedrosa
Date Submitted: September 4, 2026

Program Description:
This program contains utility functions used throughout the banking
application. It validates transaction amounts, formats currency values,
and formats transaction counts.

Reflection:
I learned how to create reusable utility functions in Python and how
helper functions can make a program more organized and easier to maintain.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""