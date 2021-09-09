# Main script

import streamlit as st
from credit import Credit

st.title('Credit calculation app')

# Sidebar
st.sidebar.title('Credit information')
st.sidebar.text('Please enter details below:')
currency = st.sidebar.selectbox('Currency:', ("€", "$", "£"))
credit_size = st.sidebar.slider('Credit size (' + currency + '):', 10000, 2000000, 500000, step=10000)
credit_duration = st.sidebar.slider('Repayment duration (years):', 1, 50, 30, step=1)
interest_rate = st.sidebar.slider('Interest rate (%):', 0., 20., 2., step=0.1) / 100

# Calculation
desired_credit = Credit(size=credit_size, duration=credit_duration, interest=interest_rate, currency=currency)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total payment", str(desired_credit.repayment_total) + currency, '+' + str(desired_credit.repayment_excess) + currency, delta_color="inverse")
col2.metric("Annual payment", str(desired_credit.repayment_annual) + currency)
col3.metric("Monthly payment", str(desired_credit.repayment_month) + currency)




