kWh = float(input())
if kWh <= 100:
    priceperkWh = 0.3
else:
    priceperkWh = 0.5
totalBill = kWh * priceperkWh
print(totalBill)