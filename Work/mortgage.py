# mortgage.py
#
# Exercise 1.7
extra_payment_start_month = int(input('extra_payment_start_month: '))
extra_payment_end_month = int(input('extra_payment_end_month: '))
extra_payment = int(input('extra_payment: '))
extra_pmt_months = range(extra_payment_start_month, extra_payment_end_month+1)

principal = 500000.0
rate = 0.05
payment = 0.0
regular_payment = 2684.11
extra_payment = regular_payment + extra_payment
total_paid = 0.0
months = 0


while principal > 0:

    months = months + 1

    if months in extra_pmt_months:
        payment = extra_payment
    else:
        payment = regular_payment

    if principal = principal * (1+rate/12) - payment <= 0:
        principal = 0.0
        total_paid = total_paid + (payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    print(f'{months}, {total_paid:.2f}, {principal:.2f}')

print(f'Total paid {total_paid:.2f}')
print(f'Number of months {months}')
