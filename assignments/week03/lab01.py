# Complete this program to classify people by age
# age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
print("-----------------------------")
age = int(input("Enter age: "))
if age >= 0 and age <= 12:
    print("you are Child")
elif age >= 13 and age <=19:
    print("you are Teenager")
elif age >= 20 and age <=59:
    print("you are Adult")
else :
    print("you are Senior")
print("-----------------------------")