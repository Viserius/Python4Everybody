try:
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
    exit()

# Standard payment: Rate multiplied with hours worked
#   Bonus payment: Stardard payment for 40 hours. Everything above bonus of 1.5
def computePay(rate, hours):
    if hours <= 40:
        return rate * hours
    else:
        return rate * 40 + (hours-40) * rate * 1.5

pay = computePay(rate, hours)
print('Pay: ', pay)