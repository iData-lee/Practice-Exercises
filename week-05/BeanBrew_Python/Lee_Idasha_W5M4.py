# Bean & Brew - Week 5, Mod 4: Rules and Repeats
print('Rules script ready')

# Task 1.1: Work out a loyalty tier 
points = 340

if points >= 500: 
    tier = 'Gold'
elif points >= 200:
    tier = 'Silver'
else: 
    tier = 'Bronze'

print(f'{points} points: {tier} member')

# Task 1.2: True, False, Boolean bool() 
print(4 < 10, 'latte' == 'Latte', 'latte' != 'mocha')
print(bool(0), bool([]), bool(None))
print(bool(0.5), bool('no'), bool('False'))

# Task 1.3: Predict, then run

#Syntax error invalid syntax. Tier must be compared '==' not assigned '='
#if tier = 'Gold': 
#    print('Show the Gold welcome screen')
#1.3b 
if tier == 'Gold': 
    print('Show the Gold welcome screen')
else: 
    print('Show the standard welcome screen')

# Task 2.1: Who gets a free drink?
is_member = True 
birthday = False 
cups_this_week = 6 

if is_member and (birthday or cups_this_week >= 5):
    print('Free Drink!')
else: 
    print('No free drink this time')

print(True or True and False)
print((True or True) and False)
print(not is_member)

# Task 2.2: Price a drink from its size code
size = 'M'

match size: 
    case 'S': 
        print('Small: $3.95') 
    case 'M': 
            print('Medium: $4.45') 
    case 'L': 
            print('Large: $4.95') 
    case _: 
            print(f'Unknown size code: {size}')    

# Task 3.1: Total the day's sales 
sales = [13.40, 4.50, 8.25, 22.10, 5.45]
total = 0 
for amount in sales: 
     total += amount 
print(f'{len(sales)} sales, total ${total:.2f}')

for batch in range(1, 4): 
     print('Brewing batch', batch)

for amount in sales: 
     if amount > 20: 
          print(f'Large sale found: ${amount:.2f}')
          break 

# Task 3.2: Number the menu 
menu_items = ['Latte', 'Cold Brew', 'Chai Latte']
for i, item in enumerate(menu_items, start=1): 
    print(f'{i}. {item}')

# Task 3.3: Label each order
orders = [
     ('Maria', 'Caramel Latte', 4.95), 
     ('James', 'House Blend', 2.75),
     ('Aisha', 'Cinnamon Roll', 3.95),
     ('Tom', 'Logo Travel Mug', 14.99),
]
for customer, item, price in orders: 
    if price >= 10:
         label = 'big ticket'
    else: 
         label = 'regular' 
    print(f'{customer} bought {item} for ${price:.2f} ({label})')

# Task 3.4 (a): Skip a cancelled order
order_no = 0
while order_no < 6:
    order_no += 1
    if order_no == 4:
        continue
    print('Serving order', order_no)

# Task 3.4 (b): Stop when the beans run low
beans_g = 1000 
while beans_g > 0: 
    beans_g -= 180 
    if beans_g < 300:
        print(f'Reorder beans! Only {beans_g} g left')
        break 
print('Beans Left:', beans_g) 


