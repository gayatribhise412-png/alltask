# Bus Seat CheckerS

# Total number of seats
N = int(input("Enter total number of seats: "))

# Reserved seats
reserved = list(map(int, input("Enter reserved seat numbers (space-separated): ").split()))

print("Available seat numbers:")

for seat in range(1, N + 1):
    if seat not in reserved:
        print(seat, end=" ")