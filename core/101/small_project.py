income = float(100)
local_state_tax = float(0.2)
federal_tax = float(0.075)

post_local_tax_income = income - (income * local_state_tax)
print(f"Post local income ${post_local_tax_income}")

post_tax_income = post_local_tax_income - (post_local_tax_income * federal_tax)
print(f"Your income ${post_tax_income}")


post_l = 100 - ((100*20)/100)
print("post local: ", post_l)

federal = (post_l*7.5)/100
final = post_l - federal
print(f"final ${final}")