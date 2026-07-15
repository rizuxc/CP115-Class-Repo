income = float(input())
if income <= 50000.0:
    totalTax = 0
else:
    if income <= 100000.0:
        totalTax = (50000 * 1/ 100) + ((income - 100000) * 2 / 100)
    else:
        totalTax = ((income - 50000) * 1/100)
print(totalTax)