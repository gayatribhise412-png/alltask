def check_password_strength(password, min_length=8):
    # len() gives number of characters
    if len(password) >= min_length:
        return "Acceptable"
    else:
        return "Not Acceptable"


pwd = input("Enter password: ")

# Function call
result = check_password_strength(pwd)


print(f"Password length: {len(pwd)}")
print(f"Status: {result}")
