# Bean & Breew - Week 5, Module 2: Register math
print('Register script ready')

# Task 1.1: Ring up an order
# 1. Define
latte_price = 4.95
muffin_price = 3.50
lattes = 2
muffins = 1

# Calculate
subtotal = latte_price * lattes + muffin_price * muffins

# Display
print(subtotal)

# Task 1.2: Turn minutes into hours
shift_min = 536
print(shift_min / 60)
print(shift_min // 60)
print(shift_min % 60)
print(2 ** 3)

# Task 1.3: Predict, then run
price = 5.00
discount = 1.00
cups = 3
total_a = price - discount * cups
total_b = (price - discount) * cups  # cashier b is correct parenthese comes first and then multiplication
print(total_a, total_b)

# Task 2.1: Order supplies
import math


cups_needed = 530
sleeve_size = 50
print(cups_needed / sleeve_size)
print(math.ceil(cups_needed / sleeve_size))
print(math.floor(cups_needed / sleeve_size))
print(math.trunc(-2.7), math.floor(-2.7))

# Task 2.2: Add tax and round
TAX_RATE = 0.0625
tax = subtotal * TAX_RATE
print(tax)
print(round(tax, 2))
print(round(3.0,2))
print(format(3.0, '.2f'))
print(type(format(tax, '.2f')))

# Tasks 2.2: Add tax and round 
TAX_RATE = 0.0625 
tax = subtotal * TAX_RATE 
print(tax)
print(round(tax, 2))
print(round(3.0, 2))
print(format(3.0, '.2f'))
print(type(format(30)))