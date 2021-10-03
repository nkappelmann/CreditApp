import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from credit import Credit

small_credit = Credit(size=1000, duration=1, interest=0.02)

def test_excess_repayment():
    assert small_credit.repayment_excess == 20

def test_total_repayment():
    assert small_credit.repayment_total == 1000 + 20