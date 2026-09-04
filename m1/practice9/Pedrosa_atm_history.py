"""
######### Learning Signature #########

Programmed by: Ken Daniel G. Pedrosa
Date Submitted: September 4, 2026

Program Description: This program retrieves transaction history
from the transactions.txt file and returns the transaction lines.

Reflection: I learned how to read transaction data from a file
and return it to the main program without printing it directly.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

def view_history():
    try:
        with open("transactions.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        return lines

    except FileNotFoundError:
        return []