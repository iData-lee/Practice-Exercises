# INCOME TAX CALCULATOR
# Name: Idasha Lee
# Date: 11/16/2026
# Description: Practice Exercise 1 - Week 6

# 2 Define the constants
TAX_RATE = .20
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 2000

# 3 Display the program title and divider line
print('Income Tax Calculator')
print('-' * 36)

# 4 Prompt for gross annual income and convert it to a float 
gross_income = float(input('Enter Gross Annual Income:'))

# 5 Prompt for the number of dependents and convert it to an int 
dependents = int(input('Enter number of dependents:'))

# 6 Calculate dependent deductions and total deductions 
dependent_deduction = DEPENDENT_DEDUCTION * dependents 
total_deductions = STANDARD_DEDUCTION + dependent_deduction
# 7 Calculate taxable income 
taxable_income = gross_income - total_deductions 

# 8 Calculate estimated income tax 
estimated_tax = taxable_income * TAX_RATE

# 9 Display income tax summary
print()
print('Income Tax Summary')
print('-' * 36)
print(f'Gross Income: ${gross_income:,.2f}')
print(f'Standard Deduction: ${STANDARD_DEDUCTION:,.2f}')
print(f'Dependent Deductions: ${dependent_deduction:,.2f}')
print(f'Total Deductions: ${total_deductions:,.2f}')
print(f'Taxable Income: ${taxable_income:,.2f}')
print(f'Tax Rate: {TAX_RATE * 100:,.2f}%')
print(f'Estimated IncomeTax: ${estimated_tax:,.2f}')