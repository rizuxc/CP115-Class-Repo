sales = int(input())

count = 0
record_days = 0
prev = 0

while sales != 0:
    count += 1
    if sales > prev:
        record_days += 1
    prev = sales
    sales = int(input())


print(count)
print(record_days)
