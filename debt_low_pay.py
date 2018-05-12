balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
myBalance = balance
minimumFixedPayment = 0

while myBalance > 0.0:
    minimumFixedPayment += 10

    for i in range(0, 12):
        myBalance -= minimumFixedPayment
        myBalance += myBalance * monthlyInterestRate

    if myBalance > 0:
        myBalance = balance

print("Lowest Payment " + str(minimumFixedPayment))