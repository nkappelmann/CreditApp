# Credit calculation app

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock

st.title('Credit calculation app')

# Define credtit class
class Credit:
    def __init__(self, size, interest=0.02, duration=30, currency='€'):
        self.size = size
        self.interest = interest
        self.duration = duration
        self.currency = currency
        self.annuity = self.calculate_annuity()
        self.repayment_annual = round(self.annuity)
        self.repayment_month = round(self.annuity / 12)
        self.repayment_total = round(self.annuity * self.duration)
        self.repayment_excess = self.repayment_total - self.size

    @st.cache
    def calculate_annuity(self):
        annuity_factor = ((1+self.interest)**self.duration * self.interest)/((1+self.interest)**self.duration-1)
        annuity = self.size*annuity_factor
        return annuity

# Sidebar
st.sidebar.title('Credit information')
st.sidebar.text('Please enter details below:')
currency = st.sidebar.selectbox('Currency:', ("€", "$", "£"))
credit_size = st.sidebar.slider(f'Credit size ({currency}):', 10_000, 2_000_000, 500_000, step=5_000)
credit_duration = st.sidebar.slider('Repayment duration (years):', 1, 50, 30, step=1)
interest_rate = st.sidebar.slider('Interest rate (%):', 0., 20., 2., step=0.05) / 100


# Calculation
desired_credit = Credit(size=credit_size, duration=credit_duration, interest=interest_rate, currency=currency)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric(
    'Total payment', f'{desired_credit.repayment_total:,}{currency}',
    f'+{desired_credit.repayment_excess:,}{currency}',
    delta_color="inverse"
)
col2.metric("Annual payment", f'{desired_credit.repayment_annual:,}{currency}')
col3.metric("Monthly payment", f'{desired_credit.repayment_month:,}{currency}')

# Pie chart
with _lock:
    fig1, ax1 = plt.subplots()
    ax1.pie(
        [desired_credit.size, desired_credit.repayment_excess],
        explode=(0, 0.1),
        labels=['Credit', 'Bank payment'],
        startangle=90, autopct='%1.1f%%',
        colors=['#66C2A5', '#FC8D62']
    )
    ax1.axis('equal')
    st.pyplot(fig1)
