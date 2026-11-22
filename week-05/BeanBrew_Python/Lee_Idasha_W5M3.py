# Bean & Brew - Week 5, Module 3: Cleaning the order data
print('Order data script ready')

# Task 1.1: Convert between types
qty_text = '12'
print(int(qty_text) + 3)
print(float(qty_text))
print(str(15) + ' cups')
print(int(7.9))
print(type(12 / 3), 12 / 3)
print(type(12 // 3), 12 // 3) 

# Task 1.2: Slice an order code
order_code = 'BB-BOS-0042'
print(order_code[0:2])
print(order_code[3:6])
print(order_code[-4:])
print(len(order_code))
print(int(order_code[-4:]))

# Task 1.3: Split a messy line
raw = '  Caramel Latte,Coffee,4.95  '
clean = raw.strip()
fields = clean.split(',')
print(fields)
print(fields[0])
print(float(fields[2]) * 2)

# Task 1.4: Clean prices and names
price_text = '1,250.00'
price = float(price_text.replace('$', '').replace(',', ''))
print(price)

answer = 'YeS'
print(answer.lower())

name = '  maria LOPEZ '
print(name.strip().title())

# Task 1.5: Ask the barista
lattes = int(input('How many lattes? '))
print(f'Total: ${lattes * 4.95:.2f}') # Value error occurred when input is three

# Task 2.1: Today's drinks in a list
drinks = ['Latte', 'Cold Brew', 'Chai']
drinks.append('Espresso')
drinks.insert(1, 'Mocha')
drinks.remove('Chai')
print(drinks)
print(len(drinks), drinks[0], drinks[-1])
drinks.sort()
print(drinks)
print('Mocha in drinks')

sales = [13.40, 4.50, 8.25]
print(round(sum(sales), 2), max(sales))

# Task 2.2: A fixed record
record = ('BB-BOS-0042','Maria', 13.40)
code, customer, amount = record 
print(customer, amount)
_, _, amount = record 
print(amount)

# Task 2.3: Unique customers
visits = ['Maria', 'James', 'Maria', 'Aisha', 'James', 'Maria']
regulars = set(visits)
print(len(visits), len(regulars))
print('Aisha' in regulars)
print('Tom' not in regulars)
regulars.add('Tom')
print(sorted(regulars))

# Task 2.4: The menu as a dictionary 
menu = {'latte': 4.95, 'cold brew': 4.50, 'chai': 4.75}
print(menu['latte'])
print(menu.get('mocha'))
print(menu.get('mocha', 'not on the menu'))

menu['mocha'] = 5.25 
menu.update({'latte': 5.10})
menu.pop('chai')
print(menu)
print(menu.keys())