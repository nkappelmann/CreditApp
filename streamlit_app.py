# Main script

# Imports
import streamlit as st
from credit import Credit
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock


# Sidebar
st.sidebar.title('Credit information')
st.sidebar.text('Please enter details below:')
currency = st.sidebar.selectbox('Currency:', ("€", "$", "£"))
credit_size = st.sidebar.slider(f'Credit size ({currency}):', 10_000, 2_000_000, 500_000, step=5_000, key='credit1_size')
credit_duration = st.sidebar.slider('Repayment duration (years):', 1, 50, 30, step=1, key='credit_duration')
interest_rate = st.sidebar.slider('Interest rate (%):', 0., 20., 2., step=0.05, key='credit1_interest_rate') / 100


# Calculate credit(s)
credit1 = Credit(
    size=credit_size, 
    duration=credit_duration, 
    interest=interest_rate, 
    currency=currency
    )

changing_interest_rate = st.sidebar.checkbox('Is the interest rate changing?')

if changing_interest_rate:
    fixed_interest_duration = st.sidebar.slider('Fixed interest duration (years):', 1, 50, 10, step=1, key='fixed_interest_duration')
    st.sidebar.text('Please enter the new interest rate below:')
    interest_rate2 = st.sidebar.slider('Interest rate (%):', 0., 20., interest_rate * 100, step=0.05, key='credit2_interest_rate') / 100

    # Define second credit
    df_credit1 = credit1.get_repayment_data()
    credit_due = float(df_credit1.loc[df_credit1['Year'] == fixed_interest_duration, 'Remaining credit'])
    credit2 = Credit(
        size=credit_due, 
        duration=credit_duration-fixed_interest_duration,
        interest=interest_rate2
        )

    repayment_total=credit1.repayment_annual * fixed_interest_duration + credit2.repayment_total

else:
    repayment_total=credit1.repayment_total


repayment_excess=repayment_total - credit_size


# Main page
st.title('Credit calculation app')

# Metrics
col1_credit1, col2_credit1, col3_credit1 = st.columns(3)
col1_credit1.metric(
    'Total payment', f'{repayment_total:,}{currency}',
    f'+{repayment_excess:,}{currency}',
    delta_color="inverse"
)

if changing_interest_rate:
    col2_credit1.metric("Annual payment (Credit #1)", f'{credit1.repayment_annual:,}{currency}')
    col3_credit1.metric("Monthly payment (Credit #1)", f'{credit1.repayment_month:,}{currency}')
    col1_credit2, col2_credit2, col3_credit2 = st.columns(3)
    col2_credit2.metric("Annual payment (Credit #2)", f'{credit2.repayment_annual:,}{currency}')
    col3_credit2.metric("Monthly payment (Credit #2)", f'{credit2.repayment_month:,}{currency}')
else:
    col2_credit1.metric("Annual payment", f'{credit1.repayment_annual:,}{currency}')
    col3_credit1.metric("Monthly payment", f'{credit1.repayment_month:,}{currency}')

# Pie chart
with _lock:
    fig1, ax1 = plt.subplots()
    ax1.pie(
        [credit_size, repayment_excess],
        explode=(0, 0.1),
        labels=['Credit', 'Bank payment'],
        startangle=90, autopct='%1.1f%%',
        colors=['#66C2A5', '#FC8D62']
    )
    ax1.axis('equal')
    st.pyplot(fig1)
