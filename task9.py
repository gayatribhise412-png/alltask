def calculate_discounted_price(price, discount_percent):
    # Calculate discount amount
    discount_amount = (price * discount_percent) / 100
    
    # Final price after discount
    discounted_price = price - discount_amount
    return discounted_price


price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))

# Function call
final_price = calculate_discounted_price(price, discount)


print(f"Original Price: {price}")
print(f"Discount {discount}%: {discount_amount:.2f}")
print(f"Final Price: {final_price:.2f}")
