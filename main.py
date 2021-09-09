# Main script

import streamlit as st
from credit import Credit

st.title('Credit calculation app')

st.text('Please enter information for the desired credit below:')

credit_size = st.slider('Credit size (€):', 10000, 2000000, 500000, step=10000)
credit_duration = st.slider('Repayment duration (years):', 1, 50, 30, step=1)
interest_rate = st.slider('Interest rate (%):', 0., 20., 2., step=0.1) / 100

desired_credit = Credit(size=credit_size, duration=credit_duration, interest=interest_rate)

col1, col2, col3 = st.columns(3)
col1.metric("Total payment", str(desired_credit.repayment_total) + '€', '+' + str(desired_credit.repayment_excess) + '€', delta_color="inverse")
col2.metric("Annual payment", str(desired_credit.repayment_annual) + '€')
col3.metric("Monthly payment", str(desired_credit.repayment_month) + '€')




