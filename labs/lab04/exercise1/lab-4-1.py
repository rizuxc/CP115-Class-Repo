kWh = float(input())
if kWh <= 100:
    totalBill = kWh * 0.3
else:
    if kWh < 200:
        totalBill = 100 * 0.3 + kWh * 0.5 - 100
    else:
        totalBill = 100 * 0.3 + 100 * 0.5 + kWh * 0.75 - 200
print(totalBill)