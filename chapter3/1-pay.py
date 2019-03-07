hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

# Standard payment: Rate multiplied with hours worked
#   Bonus payment: Stardard payment for 40 hours. Everything above bonus of 1.5
if hours <= 40:
    pay = rate * hours
else:
    pay = rate * 40 + (hours-40) * rate * 1.5

print('Pay: ', pay)