# Main script

import streamlit as st
from credit import Credit

st.title('Exploring borrowing options')

st.text('Please enter information for the desired credit below:')

credit_size = st.slider('Credit size (€):', 10000, 2000000, 500000, step=10000)
credit_duration = st.slider('Repayment duration (years):', 1, 50, 30, step=1)
interest_rate = st.slider('Interest rate (%):', 0., 20., 2., step=0.1) / 100

desired_credit = Credit(size=credit_size, duration=credit_duration, interest=interest_rate)

annuity_statement = 'Your yearly repayment is: ' + str(desired_credit.annuity.__round__())

st.text(annuity_statement)

