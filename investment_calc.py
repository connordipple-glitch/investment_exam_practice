# Version 2: Investment Calculator with Annualized Return

initial_investment = 10000
final_value = 12500
years = 3

profit = final_value - initial_investment
return_pct = (profit / initial_investment) * 100

annualized_return = (
    ((final_value / initial_investment) ** (1 / years)) - 1
) * 100

print("Investment Calculator")
print(f"Initial Investment: ${initial_investment:,.2f}")
print(f"Final Value: ${final_value:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Investment Return: {return_pct:.2f}%")
print(f"Annualized Return: {annualized_return:.2f}%")
