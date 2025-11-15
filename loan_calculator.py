import streamlit as st

st.set_page_config(page_title="Loan Calculator", page_icon="💰")

st.title("💰 Loan Calculator")

st.write("Calculate your monthly loan payment, total interest, and total payment.")

# Inputs
loan_amount = st.number_input("Loan Amount ($)", min_value=1000.0, step=1000.0)
annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.1, step=0.1)
years = st.number_input("Loan Term (Years)", min_value=1, step=1)

if st.button("Calculate"):
    # Convert annual rate to monthly and years to months
    monthly_rate = annual_rate / 100 / 12
    months = years * 12

    # Monthly payment formula
    if monthly_rate > 0:
        monthly_payment = loan_amount * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
    else:
        monthly_payment = loan_amount / months

    total_payment = monthly_payment * months
    total_interest = total_payment - loan_amount

    st.success(f"💵 Monthly Payment: ${monthly_payment:,.2f}")
    st.info(f"📈 Total Payment: ${total_payment:,.2f}")
    st.warning(f"💰 Total Interest: ${total_interest:,.2f}")
