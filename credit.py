import numpy as np
import pandas as pd

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

    def calculate_annuity(self):
        annuity_factor = ((1+self.interest)**self.duration * self.interest)/((1+self.interest)**self.duration-1)
        annuity = self.size*annuity_factor
        return annuity

    def get_repayment_data(self):
        year = range(1, self.duration + 1)
        interest_due = [self.size * self.interest]
        repayment_due = [self.repayment_annual - interest_due[0]]
        remaining_credit = [self.size - repayment_due[0]]
        if self.duration > 1:
            for i in range(2, self.duration + 1):
                interest_due.append(remaining_credit[-1] * self.interest)
                repayment_due.append(self.repayment_annual - interest_due[-1])
                remaining_credit.append(remaining_credit[-1] - repayment_due[-1])
        df = pd.DataFrame({
            'Year': list(year),
            'Interest': interest_due,
            'repayment': repayment_due,
            'Remaining credit': remaining_credit
        })
        return df

        

