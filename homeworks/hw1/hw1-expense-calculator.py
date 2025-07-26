# Monthly expense calculation program For users
"""

Personal Finance Calculator
Student: [Pongsakorn srasom]
Date: [26/07/2568]
Purpose: Calculate monthly budget and savings

"""
# กำหนดค่ารายรับรายจ่ายของตัวเองก่่อน กำหนดเป็นTHB และรับค่านั้นจากคีบอร์ดของผู้ใช้
monthly_income = float(input("Monthly income (THB): "))
rent_cost = float(input("housing cost (THB): "))
food_budget = float(input("Monthly food budget (THB): "))
transportation_cost = float(input("Monthly transportation expenses (THB): "))
entertainment_budget = float(input("Monthly entertainment budget (THB): "))
emergency_fund_percent = float(input("Percentage to save for emergency (10%): "))
investment_percent = float(input("Percentage to invest (15%): "))
# จากนั้น ใช้สูตรคำนวนค่าใช้จ่ายต่างๆ + - * /
fixed_expenses = rent_cost + transportation_cost
variable_expenses = food_budget + entertainment_budget
total_expenses = fixed_expenses + variable_expenses
remaining_income = monthly_income - total_expenses
# คำนวณเงินออม
emergency_fund = monthly_income * (emergency_fund_percent / 100)
investment_amount = monthly_income * (investment_percent / 100)
available_savings = remaining_income - emergency_fund - investment_amount
# คำนวณสัดส่วนค่าใช้จ่ายต่อรายได้
expense_ratio = (total_expenses / monthly_income) * 100
# จากนั้น แสดงผลลัพธ์ที่คำนวนจากสูตรแล้ว
print("\n=== MONTHLY BUDGET REPORT ===")
print("Income:", monthly_income, "THB")
print("Fixed Expenses:", fixed_expenses, "THB")
print("Variable Expenses:", variable_expenses, "THB")
print("Total Expenses:", total_expenses, "THB")
print("Remaining:", remaining_income, "THB")

print("\n=== SAVINGS BREAKDOWN ===")
print("Emergency Fund:", emergency_fund, "THB")
print("Investment:", investment_amount, "THB")
print("Available for Savings:", available_savings, "THB")

print("\n=== ANALYSIS ===")
print("Expense Ratio:", expense_ratio, "%")