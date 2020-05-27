income = float(input("Enter the monthly income: ")) # Ex. 100
local_state_tax = float(input("Enter the local state tax in percentage: ")) #Ex. 20% OR 0.2
federal_tax = float(input("Enter the federal tax : ")) #Ex. 7.5% OR 0.075

post_local_tax_income = income - (income * local_state_tax)
print(f"Post state tax income is ${post_local_tax_income}")

post_federal_tax_income = (post_local_tax_income * federal_tax)
print(f"Federal tax is ${post_federal_tax_income }")

net_income = post_local_tax_income - post_federal_tax_income
print(f"Your income ${net_income}")

