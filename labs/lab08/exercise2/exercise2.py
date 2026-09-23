employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

#Calculate gross salary
gross_salary = base_salary + (overtime_hours * 35)


#Selection process
if tax_status == "Single":
    if gross_salary >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status == "Married":
    if gross_salary >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
elif tax_status == "Head":
    if gross_salary >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19

net_salary = gross_salary - (gross_salary * 0.11) - (gross_salary * 0.005) - (gross_salary * tax_rate)

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
