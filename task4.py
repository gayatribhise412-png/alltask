
N = int(input("Enter number of days: "))

# Take first temperature as initial max
first_temp = float(input("Enter temperature for day 1: "))
max_temp = first_temp

# Loop from day 2 to N to find max
for i in range(2, N + 1):
    temp = float(input(f"Enter temperature for day {i}: "))
    if temp > max_temp:
        max_temp = temp

# Output
print(f"Highest temperature recorded = {max_temp}°C")