
# 1. Simple Interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si


# 2. Compound Interest
def compound_interest(p, r, t):
    amount = p * (1 + r/100) ** t
    ci = amount - p
    return ci


# 3. EMI Calculation
def emi(loan_amount, rate, years):
    """
    EMI Formula:
    EMI = [P * R * (1+R)^N] / [(1+R)^N - 1]

    P = loan amount
    R = monthly interest rate
    N = number of months
    """
    monthly_rate = rate / (12 * 100)
    months = years * 12

    emi_value = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    
    return emi_value