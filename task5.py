# Input
N = int(input("Enter number of days: "))
threshold = float(input("Enter unit threshold: "))
days_crossed = 0

# Loop to count days that crossed threshold
for i in range(1, N + 1):
    units = float(input(f"Enter units for day {i}: "))
    if units > threshold:
        days_crossed = days_crossed + 1

# Output
print(f"Number of days that crossed {threshold} units = {days_crossed}")