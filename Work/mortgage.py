# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

excess_payment = 0

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    month += 1
    principal = principal * (1+rate/12) - payment 
    total_paid = total_paid + payment
    if payment > principal:
        excess_payment = payment - principal
        total_paid = total_paid - excess_payment
    print(month, round(total_paid,2), round(principal + excess_payment, 2))
    
    
print('Total paid', round(total_paid, 2)) 
print('Months', month)
print(f'Total PAid is ${total_paid:0.2f} in {month} months')

# ans: 929,965.62 over 342 months.

