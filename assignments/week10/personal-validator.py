"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
def validate_name(name):
    # Allow alphabetic characters and spaces
    if all(part.isalpha() for part in name.split()):
        return True
    return False

def validate_age(age_str):
    if age_str.isdigit():
        age = int(age_str)
        if 18 <= age <= 65:
            return True, age
    return False, None

def validate_phone(phone):
    if phone.isdigit() and len(phone) == 10:
        return True
    return False

def get_age_group(age):
    if 18 <= age <= 30:
        return "Young Adult (18-30)"
    elif 31 <= age <= 50:
        return "Middle-Aged (31-50)"
    else:
        return "Older Adult (51-65)"

# === Program Starts Here ===
print("=== PERSONAL INFORMATION VALIDATOR ===")

name = input("Enter your name: ").strip()
age_str = input("Enter your age: ").strip()
phone = input("Enter your phone number: ").strip()

print("\nValidation Results:")

# Name Validation
if validate_name(name):
    print("Name: Valid (contains only letters and spaces)")
    formatted_name = name.upper()
else:
    print("Name: Invalid (must contain only letters and spaces)")
    formatted_name = "INVALID"

# Age Validation
valid_age, age = validate_age(age_str)
if valid_age:
    print("Age: Valid (%d years old)" % age)
    age_group = get_age_group(age)
else:
    print("Age: Invalid (must be a number between 18 and 65)")
    age_group = "INVALID"

# Phone Validation
if validate_phone(phone):
    print("Phone: Valid (10-digit number)")
    formatted_phone = "+91-" + phone
else:
    print("Phone: Invalid (must be exactly 10 digits)")
    formatted_phone = "INVALID"

# Formatted Output
print("\nFormatted Information:")
print("Name: {}".format(formatted_name))
print("Age Group: {}".format(age_group))
print("Phone: {}".format(formatted_phone))
