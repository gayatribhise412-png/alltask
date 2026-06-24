
N = int(input("Enter total number of transactions: "))
deposit_count = 0
withdrawal_count = 0


for i in range(1, N + 1):
    txn = float(input(f"Enter transaction {i}: "))
    
    if txn > 0:
        deposit_count = deposit_count + 1
    elif txn < 0:
        withdrawal_count = withdrawal_count + 1
    


print(f"Total Deposits: {deposit_count}")
print(f"Total Withdrawals: {withdrawal_count}")