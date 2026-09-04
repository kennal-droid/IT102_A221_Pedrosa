from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, name, pin, starting_balance):
        self.account_number = account_number
        self.account_name = name
        self._pin = pin
        self._balance = starting_balance
        self.savings_goal = None
        self.savings_target = 0

    def check_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance < 0:
            return False

        self._balance = balance
        return True

    def deposit(self, amount):
        if amount <= 0:
            return False

        self._balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount
        return True

    def verify_pin(self, pin):
        return self._pin == pin

    def change_pin(self, current_pin, new_pin):
        if not self.verify_pin(current_pin):
            return False

        if len(new_pin) != 4 or not new_pin.isdigit():
            return False

        self._pin = new_pin
        return True

    def get_pin(self):
        return self._pin

    def set_savings_goal(self, goal_name, target_amount):
        if not goal_name.strip() or target_amount <= 0:
            return False

        self.savings_goal = goal_name
        self.savings_target = target_amount
        return True

    def get_savings_goal(self):
        return self.savings_goal, self.savings_target

    @abstractmethod
    def get_account_type(self):
        pass


class SavingsAccount(BankAccount):

    def get_account_type(self):
        return "Savings Account"


class StudentAccount(BankAccount):

    def get_account_type(self):
        return "Student Account"

"""
######### Learning Signature #########

Programmed by: Ken Daniel G. Pedrosa
Date Submitted: September 4, 2026

Program Description:
This program defines the bank account classes used in the banking application.
It demonstrates Encapsulation, Abstraction, Inheritance, and Polymorphism
through the BankAccount, SavingsAccount, and StudentAccount classes.

Reflection:
I learned how to use classes, inheritance, abstract methods, and encapsulation
to organize the banking system and make the code more secure and reusable.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""