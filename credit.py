class Credit:
    def __init__(self, size, interest=0.02, duration=30):
        self.size = size
        self.interest = interest
        self.duration = duration
        self.annuity = self.calculate_annuity()

    def calculate_annuity(self):
        annuity_factor = ((1+self.interest)**self.duration * self.interest)/((1+self.interest)**self.duration-1)
        annuity = self.size*annuity_factor
        return annuity
