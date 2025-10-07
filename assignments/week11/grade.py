"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""
# Global variable for passing grade
passing_grade = 50

def input_students(num_students):
    """
    Prompts the user to input name and 3 scores for each student.
    Returns a list of student dictionaries.
    """
    students = []
    for i in range(num_students):
        print(f"\nEnter data for student {i + 1}:")
        name = input("Name: ")
        scores = []
        for j in range(3):
            score = float(input(f"Score {j + 1}: "))
            scores.append(score)
        students.append({'name': name, 'scores': scores})
    return students

def calculate_averages(students):
    """
    Calculates average score for each student and adds it to their dictionary.
    Modifies the original list (shows list mutability).
    """
    for student in students:
        total = 0
        for score in student['scores']:
            total += score
        average = total / len(student['scores'])
        student['average'] = average  # Mutating the original list

def display_results(students):
    """
    Displays each student's name, average, and pass/fail status.
    """
    print("\n--- Student Results ---")
    for student in students:
        status = "PASS" if student['average'] >= passing_grade else "FAIL"
        print(f"{student['name']}: Average = {student['average']:.2f} - {status}")

# Example usage
if __name__ == "__main__":
    num = int(input("Enter number of students: "))
    student_list = input_students(num)
    calculate_averages(student_list)
    display_results(student_list)
