# ######### Learning Signature #########
#
# Programmed by: Ken Daniel G. Pedrosa
# Date Submitted: September 4, 2026
#
# Program Description: This program is a Streamlit-based digital
# banking application with account management, transactions,
# money transfer, PIN management, savings goals, and e-receipts.
#
# Reflection: I learned how to extend an existing OOP banking
# application by adding new modular features and connecting
# them to a graphical user interface.
#
# AI Usage
# [ ] No AI Assistance – Completed independently without AI.
# [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [x] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
#
# ######### Learning Signature #########


import streamlit as st
import Pedrosa_bank_auth
import Pedrosa_bank_storage
import Pedrosa_bank_transactions
import Pedrosa_bank_analysis
import Pedrosa_bank_utils
import Pedrosa_bank_transfer
import Pedrosa_bank_savings
import Pedrosa_bank_receipt


# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="Pedrosa Digital Bank",
    page_icon="🏦",
    layout="wide"
)


# =========================
# CUSTOM UI
# =========================

st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 18px;
        color: #777777;
        margin-bottom: 25px;
    }

    .balance-card {
        padding: 25px;
        border-radius: 15px;
        background-color: #f0f4f8;
        margin-bottom: 20px;
    }

    .balance-label {
        font-size: 16px;
        color: #666666;
    }

    .balance-value {
        font-size: 34px;
        font-weight: bold;
    }

    .section-title {
        font-size: 26px;
        font-weight: bold;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)


# =========================
# SESSION STATE
# =========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "account" not in st.session_state:
    st.session_state.account = None


# =========================
# LOGIN / REGISTER
# =========================

if not st.session_state.logged_in:

    st.markdown(
        '<div class="main-title">🏦 Pedrosa Digital Bank</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Simple, secure, and convenient banking</div>',
        unsafe_allow_html=True
    )

    login_tab, register_tab = st.tabs(
        ["🔐 Login", "📝 Register Account"]
    )

    # -------------------------
    # LOGIN
    # -------------------------

    with login_tab:

        st.subheader("Welcome Back")

        account_number = st.text_input(
            "Account Number",
            key="login_account"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
            key="login_pin"
        )

        if st.button(
            "🔐 Login",
            use_container_width=True
        ):

            account, message = Pedrosa_bank_auth.login_account(
                account_number.strip(),
                pin.strip()
            )

            if account is not None:

                st.session_state.logged_in = True
                st.session_state.account = account

                st.success(message)
                st.rerun()

            else:
                st.error(message)

    # -------------------------
    # REGISTER
    # -------------------------

    with register_tab:

        st.subheader("Create a New Account")

        with st.form("registration_form"):

            name = st.text_input("Full Name")

            new_account_number = st.text_input(
                "Account Number"
            )

            new_pin = st.text_input(
                "Create 4-Digit PIN",
                type="password",
                max_chars=4
            )

            confirm_pin = st.text_input(
                "Confirm PIN",
                type="password",
                max_chars=4
            )

            account_type = st.selectbox(
                "Account Type",
                [
                    "Savings Account",
                    "Student Account"
                ]
            )

            starting_balance = st.number_input(
                "Starting Balance",
                min_value=0.0,
                step=100.0
            )

            register_button = st.form_submit_button(
                "📝 Create Account",
                use_container_width=True
            )

        if register_button:

            account, message = Pedrosa_bank_auth.register_account(
                new_account_number.strip(),
                name.strip(),
                new_pin.strip(),
                confirm_pin.strip(),
                account_type,
                starting_balance
            )

            if account is not None:
                st.success(message)
                st.info(
                    "Your account has been created. "
                    "You can now log in using your account number and PIN."
                )
            else:
                st.error(message)


# =========================
# MAIN BANKING APPLICATION
# =========================

else:

    account = st.session_state.account

    # -------------------------
    # SIDEBAR
    # -------------------------

    with st.sidebar:

        st.title("🏦 Pedrosa Bank")

        st.write(
            f"Welcome, **{account.account_name}**"
        )

        st.divider()

        page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "💰 Deposit",
                "💸 Withdraw",
                "🔄 Money Transfer",
                "🔐 Change PIN",
                "🎯 Savings Goal",
                "🧾 E-Receipt",
                "📜 Transaction History",
                "📊 Transaction Analysis"
            ]
        )

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False
            st.session_state.account = None

            st.rerun()

    # -------------------------
    # DASHBOARD
    # -------------------------

    if page == "🏠 Dashboard":

        st.markdown(
            '<div class="main-title">Dashboard</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="subtitle">Your account overview</div>',
            unsafe_allow_html=True
        )

        balance = account.check_balance()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "💰 Current Balance",
                Pedrosa_bank_utils.format_currency(balance)
            )

        with col2:
            st.metric(
                "👤 Account Holder",
                account.account_name
            )

        with col3:
            st.metric(
                "🏦 Account Type",
                account.get_account_type()
            )

        st.divider()

        st.subheader("Account Information")

        info1, info2 = st.columns(2)

        with info1:
            st.write(
                f"**Account Number:** {account.account_number}"
            )

        with info2:
            st.write(
                f"**Account Type:** {account.get_account_type()}"
            )

        st.info(
            "Use the navigation menu on the left to manage your account."
        )

    # -------------------------
    # DEPOSIT
    # -------------------------

    elif page == "💰 Deposit":

        st.title("💰 Deposit Money")

        st.write(
            "Add money to your bank account."
        )

        st.metric(
            "Current Balance",
            Pedrosa_bank_utils.format_currency(
                account.check_balance()
            )
        )

        amount = st.number_input(
            "Deposit Amount",
            min_value=0.0,
            step=100.0
        )

        if st.button(
            "💰 Make Deposit",
            use_container_width=True
        ):

            if not Pedrosa_bank_utils.is_valid_amount(amount):

                st.error(
                    "Please enter an amount greater than zero."
                )

            elif account.deposit(amount):

                Pedrosa_bank_storage.update_account(account)

                Pedrosa_bank_transactions.record_transaction(
                    account,
                    "Deposit",
                    amount
                )

                st.success(
                    f"Successfully deposited "
                    f"{Pedrosa_bank_utils.format_currency(amount)}"
                )

                st.rerun()

            else:
                st.error("Deposit failed.")

    # -------------------------
    # WITHDRAW
    # -------------------------

    elif page == "💸 Withdraw":

        st.title("💸 Withdraw Money")

        st.write(
            "Withdraw money from your bank account."
        )

        st.metric(
            "Current Balance",
            Pedrosa_bank_utils.format_currency(
                account.check_balance()
            )
        )

        amount = st.number_input(
            "Withdrawal Amount",
            min_value=0.0,
            step=100.0
        )

        if st.button(
            "💸 Make Withdrawal",
            use_container_width=True
        ):

            if not Pedrosa_bank_utils.is_valid_amount(amount):

                st.error(
                    "Please enter an amount greater than zero."
                )

            elif account.withdraw(amount):

                Pedrosa_bank_storage.update_account(account)

                Pedrosa_bank_transactions.record_transaction(
                    account,
                    "Withdraw",
                    amount
                )

                st.success(
                    f"Successfully withdrew "
                    f"{Pedrosa_bank_utils.format_currency(amount)}"
                )

                st.rerun()

            else:

                st.error(
                    "Withdrawal failed. "
                    "You may not have enough balance."
                )

    # -------------------------
    # MONEY TRANSFER
    # -------------------------

    elif page == "🔄 Money Transfer":

        st.title("🔄 Money Transfer")

        st.write(
            "Transfer money to another registered account."
        )

        recipient_number = st.text_input(
            "Recipient Account Number"
        )

        amount = st.number_input(
            "Transfer Amount",
            min_value=0.0,
            step=100.0
        )

        if st.button(
            "🔄 Transfer Money",
            use_container_width=True
        ):

            if not Pedrosa_bank_utils.is_valid_amount(amount):

                st.error(
                    "Please enter an amount greater than zero."
                )

            else:

                recipient = Pedrosa_bank_storage.find_account(
                    recipient_number.strip()
                )

                success, message = (
                    Pedrosa_bank_transfer.transfer_money(
                        account,
                        recipient,
                        amount
                    )
                )

                if success:

                    Pedrosa_bank_storage.update_account(account)
                    Pedrosa_bank_storage.update_account(recipient)

                    Pedrosa_bank_transactions.record_transaction(
                        account,
                        "Transfer",
                        amount
                    )

                    st.success(message)

                    st.info(
                        f"Transferred "
                        f"{Pedrosa_bank_utils.format_currency(amount)} "
                        f"to account {recipient.account_number}."
                    )

                    st.rerun()

                else:

                    st.error(message)

    # -------------------------
    # CHANGE PIN
    # -------------------------

    elif page == "🔐 Change PIN":

        st.title("🔐 Change PIN")

        st.write(
            "Update your account PIN securely."
        )

        current_pin = st.text_input(
            "Current PIN",
            type="password",
            max_chars=4
        )

        new_pin = st.text_input(
            "New PIN",
            type="password",
            max_chars=4
        )

        confirm_pin = st.text_input(
            "Confirm New PIN",
            type="password",
            max_chars=4
        )

        if st.button(
            "🔐 Change PIN",
            use_container_width=True
        ):

            if new_pin != confirm_pin:

                st.error(
                    "New PINs do not match."
                )

            elif account.change_pin(
                current_pin.strip(),
                new_pin.strip()
            ):

                Pedrosa_bank_storage.update_account(
                    account
                )

                st.success(
                    "Your PIN has been changed successfully."
                )

            else:

                st.error(
                    "Invalid current PIN or new PIN. "
                    "The new PIN must contain exactly 4 digits."
                )

    # -------------------------
    # SAVINGS GOAL
    # -------------------------

    elif page == "🎯 Savings Goal":

        st.title("🎯 Savings Goal")

        st.write(
            "Set a target and track your savings progress."
        )

        goal_name = st.text_input(
            "Goal Name",
            placeholder="Example: New Laptop"
        )

        target_amount = st.number_input(
            "Target Amount",
            min_value=0.0,
            step=500.0
        )

        if st.button(
            "🎯 Create Savings Goal",
            use_container_width=True
        ):

            success, message = (
                Pedrosa_bank_savings.create_savings_goal(
                    account,
                    goal_name,
                    target_amount
                )
            )

            if success:

                Pedrosa_bank_storage.update_account(
                    account
                )

                st.success(message)

            else:

                st.error(message)

        progress = (
            Pedrosa_bank_savings.get_savings_progress(
                account
            )
        )

        if progress:

            st.divider()

            st.subheader(
                f"🎯 {progress['goal_name']}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Current Balance",
                    f"₱{progress['current']:,.2f}"
                )

            with col2:

                st.metric(
                    "Savings Target",
                    f"₱{progress['target']:,.2f}"
                )

            st.progress(
                progress["progress"] / 100
            )

            st.write(
                f"**{progress['progress']:.1f}% completed**"
            )

    # -------------------------
    # E-RECEIPT
    # -------------------------

    elif page == "🧾 E-Receipt":

        st.title("🧾 E-Receipt")

        st.write(
            "Generate a digital receipt for your banking activity."
        )

        transaction_type = st.selectbox(
            "Transaction Type",
            [
                "Deposit",
                "Withdraw",
                "Transfer"
            ]
        )

        amount = st.number_input(
            "Transaction Amount",
            min_value=0.0,
            step=100.0
        )

        if st.button(
            "🧾 Generate E-Receipt",
            use_container_width=True
        ):

            if not Pedrosa_bank_utils.is_valid_amount(amount):

                st.error(
                    "Please enter an amount greater than zero."
                )

            else:

                receipt = (
                    Pedrosa_bank_receipt.generate_receipt(
                        account,
                        transaction_type,
                        amount,
                        account.check_balance()
                    )
                )

                st.code(receipt)

                Pedrosa_bank_receipt.save_receipt(
                    receipt
                )

                st.success(
                    "E-Receipt generated and saved successfully."
                )

    # -------------------------
    # TRANSACTION HISTORY
    # -------------------------

    elif page == "📜 Transaction History":

        st.title("📜 Transaction History")

        transactions = (
            Pedrosa_bank_transactions.get_transactions()
        )

        account_transactions = [
            transaction
            for transaction in transactions
            if transaction["account_number"]
            == account.account_number
        ]

        if not account_transactions:

            st.info(
                "No transactions found for this account."
            )

        else:

            st.write(
                Pedrosa_bank_utils.format_transaction_count(
                    len(account_transactions)
                )
            )

            for transaction in reversed(account_transactions):

                with st.container(border=True):

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.write(
                            f"**{transaction['transaction']}**"
                        )
                        st.caption(
                            transaction["timestamp"]
                        )

                    with col2:
                        st.write(
                            f"Amount: ₱{transaction['amount']}"
                        )

                    with col3:
                        st.write(
                            f"Balance: ₱{transaction['balance_after']}"
                        )

    # -------------------------
    # TRANSACTION ANALYSIS
    # -------------------------

    elif page == "📊 Transaction Analysis":

        st.title("📊 Transaction Analysis")

        transactions = (
            Pedrosa_bank_transactions.get_transactions()
        )

        account_transactions = [
            transaction
            for transaction in transactions
            if transaction["account_number"]
            == account.account_number
        ]

        analysis = Pedrosa_bank_analysis.analyze_transactions(
            account_transactions
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Transactions",
                analysis["total_transactions"]
            )

        with col2:
            st.metric(
                "Deposits",
                analysis["deposits"]
            )

        with col3:
            st.metric(
                "Withdrawals",
                analysis["withdrawals"]
            )

        st.divider()

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric(
                "Total Deposited",
                Pedrosa_bank_utils.format_currency(
                    analysis["total_deposited"]
                )
            )

        with col5:
            st.metric(
                "Total Withdrawn",
                Pedrosa_bank_utils.format_currency(
                    analysis["total_withdrawn"]
                )
            )

        with col6:
            st.metric(
                "Net Cash Flow",
                Pedrosa_bank_utils.format_currency(
                    analysis["net_cash_flow"]
                )
            )

        st.divider()

        col7, col8 = st.columns(2)

        with col7:
            st.metric(
                "Largest Transaction",
                Pedrosa_bank_utils.format_currency(
                    analysis["largest_transaction"]
                )
            )

        with col8:
            st.metric(
                "Average Transaction",
                Pedrosa_bank_utils.format_currency(
                    analysis["average_transaction"]
                )
            )

        st.subheader("Transaction Ratios")

        ratio1, ratio2 = st.columns(2)

        with ratio1:
            st.write(
                f"Deposit Ratio: "
                f"{analysis['deposit_ratio']:.1f}%"
            )

        with ratio2:
            st.write(
                f"Withdrawal Ratio: "
                f"{analysis['withdrawal_ratio']:.1f}%"
            )