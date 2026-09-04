import streamlit as st

# TODO 1:
# Import the Account class.
from Pedrosa_atm_account import Account

# TODO 2:
# Import the balance module.
import Pedrosa_atm_balance as balance

# TODO 3:
# Import the deposit module.
import Pedrosa_atm_deposit as deposit

# TODO 4:
# Import the withdraw module.
import Pedrosa_atm_withdraw as withdraw

# TODO 5:
# Import the history module.
import Pedrosa_atm_history as history

# TODO 6:
# Import the analysis module.
import Pedrosa_atm_analysis as analysis


# TODO 7:
# Create the Account object.
if "account" not in st.session_state:
    st.session_state.account = Account("Juan Dela Cruz", 10000.00)

account = st.session_state.account


# TODO 8:
# Configure the Streamlit page.
st.set_page_config(
    page_title="ATM System",
    page_icon="🏦",
    layout="wide"
)


# TODO 9:
# Create the main ATM title.
st.title("🏦 ATM System")


# TODO 10:
# Display the welcome message.
st.write(f"Welcome, {account.account_name}!")


# TODO 11:
# Add a divider.
st.divider()


# TODO 12:
# Create the sidebar menu.
st.sidebar.title("ATM Menu")


# TODO 13:
# Allow the user to select an operation.
option = st.sidebar.radio(
    "Select an operation:",
    [
        "Check Balance",
        "Deposit",
        "Withdraw",
        "View History",
        "Analyze Transactions"
    ]
)


# CHECK BALANCE
if option == "Check Balance":

    st.header("Check Balance")

    current_balance = balance.check_balance(account)

    st.metric(
        "Current Balance",
        f"₱{current_balance:,.2f}"
    )


# DEPOSIT
elif option == "Deposit":

    st.header("Deposit Money")

    amount = st.number_input(
        "Enter deposit amount:",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Deposit Money"):

        if amount <= 0:
            st.error("Invalid deposit amount.")

        else:
            result = deposit.deposit_money(account, amount)

            if result:
                st.success("Deposit successful!")

                st.metric(
                    "New Balance",
                    f"₱{account.check_balance():,.2f}"
                )

            else:
                st.error("Deposit failed.")


# WITHDRAW
elif option == "Withdraw":

    st.header("Withdraw Money")

    amount = st.number_input(
        "Enter withdrawal amount:",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Withdraw Money"):

        if amount <= 0:
            st.error("Invalid withdrawal amount.")

        elif amount > account.check_balance():
            st.error("Insufficient balance.")

        else:
            result = withdraw.withdraw_money(account, amount)

            if result:
                st.success("Withdrawal successful!")

                st.metric(
                    "New Balance",
                    f"₱{account.check_balance():,.2f}"
                )

            else:
                st.error("Withdrawal failed.")


# VIEW HISTORY
elif option == "View History":

    st.header("Transaction History")

    lines = history.view_history()

    if lines:
        st.text("".join(lines))

    else:
        st.info("No transactions found.")


# ANALYZE TRANSACTIONS
elif option == "Analyze Transactions":

    st.header("Transaction Analysis")

    results = analysis.analyze_transactions()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Transactions",
            results["total_transactions"]
        )

        st.metric(
            "Deposits",
            results["deposits"]
        )

        st.metric(
            "Withdrawals",
            results["withdrawals"]
        )

    with col2:
        st.metric(
            "Total Deposited",
            f"₱{results['total_deposited']:,.2f}"
        )

        st.metric(
            "Total Withdrawn",
            f"₱{results['total_withdrawn']:,.2f}"
        )

        st.metric(
            "Average Transaction",
            f"₱{results['average_transaction']:,.2f}"
        )

    with col3:
        st.metric(
            "Largest Transaction",
            f"₱{results['largest_transaction']:,.2f}"
        )

        st.write(
            f"**Latest Transaction:** "
            f"{results['latest_transaction'] or 'None'}"
        )

        st.write(
            f"**Latest Activity:** "
            f"{results['latest_timestamp'] or 'None'}"
        )

