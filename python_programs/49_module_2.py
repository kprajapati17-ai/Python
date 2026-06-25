import financial_tools

# Simple Interest
si = financial_tools.simple_interest(10000, 5, 2)
print("Simple Interest:", si)

# Compound Interest
ci = financial_tools.compound_interest(10000, 5, 2)
print("Compound Interest:", ci)

# EMI
emi_val = financial_tools.emi(500000, 10, 5)
print("Monthly EMI:", emi_val)