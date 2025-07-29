"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    person = ("JAY", 19, "saraburi", "Thailand")
    hobbies = []
    while True:
        print("\nWhat do you want to do?")
        print("1: Display all information")
        print("2: Add hobby")
        print("3: Remove hobby")
        print("4: Edit age")
        print("5: Exit")
        choice = input("Enter your choice: ")
        
        # Display all information
        if choice == "1":
            print("Name:", person[0])
            print("Age:", person[1])
            print("City:", person[2])
            print("Country:", person[3])
            print("Hobbies:", hobbies)
        # Add new hobbies
        elif choice == "2":
            hobby = input("Enter a new hobby: ")
            hobbies.append(hobby)
        # Remove hobbies
        elif choice == "3":
            hobby = input("Enter the hobby to remove: ")
            if hobby in hobbies:
                hobbies.remove(hobby)
        # Update age (by creating a new tuple)n
        elif choice == "4":
            age = input("Enter new age: ")
            if age.isdigit():
                person = (person[0], int(age), person[2], person[3])
        # Exit
        elif choice == "5":
            break

if __name__ == "__main__":
    personal_info_manager()