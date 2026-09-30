num_rounds = int(input())

final_score = 0
rounds_processed = 0

for i in range(num_rounds):
    score = int(input())
    if score > 100:
        bonus = 0.20
        final_score += score + bonus
    else:
        final += score

print(f"{final_score:.1f}")
print(rounds_processed)
cp115_env\Scripts\activate