from Pedrosa_atm_account import Account

# Create account with starting balance
account = Account("Juan Dela Cruz", 10000.00)

# Test 1 — Starting balance
print(f"Starting balance: ₱{account.check_balance():.2f}")

# Test 2 — Successful withdrawal
result = account.withdraw(2000.00)

if result:
    print("Withdrawal successful.")
    print(f"New Balance: ₱{account.check_balance():.2f}")
else:
    print("Withdrawal failed.")

print()

# Test 3 — Insufficient balance
result = account.withdraw(15000.00)

if result:
    print("Withdrawal successful.")
else:
    print("Insufficient balance.")

print(f"Final Balance: ₱{account.check_balance():.2f}")