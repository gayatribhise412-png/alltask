def calculate_final_salary(basic_salary, bonus_percent):
    # Calculate bonus amount
    bonus_amount = (basic_salary * bonus_percent) / 100
    
    # Final salary = basic + bonus
    final_salary = basic_salary + bonus_amount
    return final_salary


basic = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus percentage: "))


final = calculate_final_salary(basic, bonus)


print(f"Basic Salary: {basic}")
print(f"Bonus {bonus}%: {final - basic}")
print(f"Final Salary: {final}")