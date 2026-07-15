kWh = float(input())
if kWh <= 100:
    totalBill = kWh * 0.3
else:
    if kWh < 200:
        totalBill = 100 * 0.3 + kWh - 100 * 0.5
    else:
        totalBill = 100 * 0.3 + 100 * 0.5 + kWh - 200 * 0.75
print(totalBill)
