# eg 7th budget calculator

income = float(input("What is your monthly income: "))
rent = float(input("What is your monthly rent/mortgage: "))
utilities = float(input("What is your monthly utilities: "))
groceries = float(input("What is your monthly groceries: "))
transportation = float(input("What is your monthly transportation: "))

rent_pct = rent / income * 100
utilities_pct = utilities / income * 100
groceries_pct = groceries / income * 100
transportation_pct = transportation / income * 100

save = income * 0.10
spending_money = income - (rent + utilities + groceries + transportation + save)
print(f"\nYour rent is ${rent:.2f} and that is {rent_pct:.0f}% of your income.")
print(f"Your utilities are ${utilities:.2f} and that is {utilities_pct:.0f}% of your income.")
print(f"Your groceries are ${groceries:.2f} and that is {groceries_pct:.0f}% of your income.")
print(f"Your transportation is ${transportation:.2f} and that is {transportation_pct:.0f}% of your income.")
print(f"\nYou should save ${save:.2f} a month, that is 10% of your income.")
print(f"\nYou have ${spending_money:.2f} of spending money.")




