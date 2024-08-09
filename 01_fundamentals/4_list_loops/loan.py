money_owned = 50000
apr = 3
payment = 1000
months = 64

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owned*monthly_rate

    money_owned = money_owned + interest_paid

    if (money_owned - payment < 0):
        print('The last payment is', money_owned)
        print('You paid off the loan in', i+1, 'months')
        break
    money_owned = money_owned - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest', end=' ')
    print('Now I owe ', money_owned)
