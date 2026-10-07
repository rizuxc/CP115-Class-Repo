speed = int(input())

running_streak = 0
longest_streak = 0
total_readings = 0

while speed != -1:
    total_readings += 1
    if speed < 20:
        running_streak += 1
    else:
        running_streak = 0

    if running_streak > longest_streak:
        longest_streak = running_streak
        
    speed = int(input())

print(total_readings)
print(longest_streak)
