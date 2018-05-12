balance = 42
annual_interest_rate = 0.2
monthly_payment_rate = 0.04
for i in range(1, 13):
    monthly_interest_rate = (annual_interest_rate / 12.0)
    min_month_pay = (monthly_payment_rate * balance)
    monthly_unpaid_balance = (balance - min_month_pay)
    updated_balance = (monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance))
    balance = updated_balance
    print('Month %s Remaining balance: %s' % (i, round(updated_balance, 2)))
