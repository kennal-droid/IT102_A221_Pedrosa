# ######### Learning Signature #########
#
# Programmed by: Ken Daniel G. Pedrosa
# Date Submitted: September 4, 2026
#
# Program Description: This program handles money transfers
# between registered bank accounts.
#
# Reflection: I learned how to create a modular money transfer
# feature that validates accounts and transfer amounts.
#
# AI Usage
# [ ] No AI Assistance – Completed independently without AI.
# [X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
#
# ######### Learning Signature #########




def transfer_money(sender, receiver, amount):
    if amount <= 0:
        return False, "Transfer amount must be greater than zero."

    if receiver is None:
        return False, "Recipient account not found."

    if sender.account_number == receiver.account_number:
        return False, "You cannot transfer money to your own account."

    if amount > sender.check_balance():
        return False, "Insufficient balance."

    sender.withdraw(amount)
    receiver.deposit(amount)

    return True, "Money transfer successful."