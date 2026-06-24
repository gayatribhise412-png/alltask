
N = int(input("Enter number of days: "))
total_sales = 0


for i in range(1, N + 1):
    sale = float(input(f"Enter sales for day {i}: "))
    total_sales = total_sales + sale


print(f"Total Sales = {total_sales}")