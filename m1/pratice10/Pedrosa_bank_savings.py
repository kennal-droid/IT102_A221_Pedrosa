# ######### Learning Signature #########
#
# Programmed by: Ken Daniel G. Pedrosa
# Date Submitted: September 4, 2026
#
# Program Description: This program allows users to create
# and monitor a personal savings goal.
#
# Reflection: I learned how to create a savings goal feature
# and calculate the user's progress toward a target amount.
#
# AI Usage
# [ ] No AI Assistance – Completed independently without AI.
# [X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
#
# ######### Learning Signature #########
#
# ######### Learning Signature #########



def create_savings_goal(account, goal_name, target_amount):
    if target_amount <= 0:
        return False, "Target amount must be greater than zero."

    if not goal_name.strip():
        return False, "Goal name cannot be empty."

    account.set_savings_goal(goal_name, target_amount)

    return True, "Savings goal created successfully."


def get_savings_progress(account):
    goal_name, target_amount = account.get_savings_goal()

    if goal_name is None:
        return None

    current_balance = account.check_balance()

    if target_amount == 0:
        progress = 0
    else:
        progress = (current_balance / target_amount) * 100

    if progress > 100:
        progress = 100

    return {
        "goal_name": goal_name,
        "target": target_amount,
        "current": current_balance,
        "progress": progress
    }