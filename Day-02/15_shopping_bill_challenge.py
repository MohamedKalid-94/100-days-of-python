# Day 2 - Extra Practice
# Shopping Bill Calculator

print("================================")
print("     SHOPPING BILL CALCULATOR")
print("================================")

# Get product details from the user

product_name = input("Enter the product name: ")
product_price = float(input("Enter the product price: ₹"))
quantity = int(input("Enter the quantity: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the subtotal

subtotal = product_price * quantity

# Calculate the discount amount

discount_amount = subtotal * discount_percentage / 100

# Calculate the final price

final_price = subtotal - discount_amount

# Display the bill

print()
print("================================")
print("          BILL SUMMARY")
print("================================")

print(f"Product: {product_name}")
print(f"Price per item: ₹{product_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount: {discount_percentage:.2f}%")
print(f"Discount amount: ₹{discount_amount:.2f}")
print(f"Final price: ₹{final_price:.2f}")

print("================================")
print("       Thank you for shopping!")
print("================================")