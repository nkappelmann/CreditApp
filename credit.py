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
