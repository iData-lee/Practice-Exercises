# Bean & Breww - Week 5, Module 1
#print('Python is ready!')

# Task 1.1: Say Hello
#print('Welcome to Bean & Brew Coffee Co.!')
#print("Today's special: Caramel Latte")
#print('Stores:', 3)

# Task 1.2: Store the store's facts in variables
store_name = 'Back Bay'
open_hour = 7
latte_price = 4.95
is_open = True
manager = None 
MAX_SEATS = 40

#print(store_name, open_hour, latte_price, is_open, manager, MAX_SEATS)

# Task 1.3: Comment your code
# Author: Idasha Lee
#print('Comments are ignored by Python')   # this note is not printed

# Task 1.4: Check the data types
# Store name is a string
# open hour is a integer
# latte price is a float
# is open is a boolean
# manager is a NoneType
# '7' is a string

#print(type(store_name))
#print(type(open_hour))
#print(type(latte_price))
#print(type(is_open))
#print(type(manager))
#print(type('7'))

# Task 1.5: Predict, then run
cups_sold = 120
#print('Cups sold today:' + cups_sold)   # There are no quotes to distinguish that cups sold is a variable. Using the f string could be a better option.
# The error explains that only strings can be concatenated and not intergers

#print('Cups sold today: ' + str(cups_sold))
#print(cups_sold + cups_sold)
#print('120' + '120')

#Task 2.1: Predict, then run
#print(store_nme) # Broken: commented out
# The error code states that the name is not defined. And gave a suggestion for the closest name it could reference to.
print(store_name)

# Task 2.2 (a) Predict, then run
#print('Back Bay opens at', open_hour
# The error code shows that the '(' was never closed. It doesnt show the previous print either.

#Task 2.2 (b) 
#print('line one')
 #   print('line two')
# The error code states there was an unexpected indent and shows which line was indented incorrectly.

# Fixed versions of (a) and (b)
print('Back Bay opens at', open_hour)
print('line one')
print('line two')

# Task 2.3: Predict, then run
#qty = int('twelve')
# Inputing the text version of the word twelve can not be processed due to it not containing digits.

qty = int('12')
print(qty + 1)

#Task 3.1 Bonus
#(a) 
# #class = 'VIP'
# Class is a keyword used in python used to define classes so it cannot be used as a variable name.

#(b)
#2nd_store = 'Kendall Square'
# The variable name begins with a digit so python reads the beginning as a number.

#(c): valid names
customer_class = 'VIP'
store_2 = 'Kendall Square'
print(customer_class, store_2)

