score = int(input())

count = 0
total_a = 0
total_b = 0
winner = 0

while score != -1:
    count += 1
    if count % 2 == 0:
        total_b += score
    else:
        total_a += score

    if total_a > total_b:
        winner = "A"
    elif total_b > total_a:
        winner = "B"
    else:
        winner = "Tie"
    
    score = int(input())

print(total_a)
print(total_b)
print(winner)
