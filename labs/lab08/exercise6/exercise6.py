position = input()
overtime_hours = int(input())
is_weekend = input()

#Determining the base hourly rate based on employee position
if position == "Manager":
    base_rate = 30
elif position == "Supervisor":
    base_rate = 20
elif position == "Staff":
    base_rate = 15
else:
    base_rate = 8

#Calculating overtime pay
if overtime_hours <= 8:
    extra_pay = base_rate * 1.5
else:
    extra_pay = (base_rate - 8) * 2

if is_weekend == "yes":
    overtime_pay = (overtime_hours * 5) + extra_pay

print(overtime_pay)
