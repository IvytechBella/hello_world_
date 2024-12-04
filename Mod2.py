# Author: Isabella Carman
# File Name: Mod2.py
# Description: This Python app accepts student names and GPAs, checks if they qualify for the Dean's List or Honor Roll, 
#           and prints the respective messages. Processing stops when the last name 'ZZZ' is entered.

def main():
    while True:
        # Input of last name of the student
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()

        # Exit the loop if the user enters 'ZZZ' 
        if last_name.upper() == 'ZZZ':
            print("Exiting the program.")
            break

        # Input of the first name of the student
        first_name = input("Enter the student's first name: ").strip()

        try:
            # Get the GPA of the student and convert it to a float
            gpa = float(input("Enter the student's GPA: "))

            # Check if the student qualifies for Dean's List or Honor Roll
            if gpa >= 3.5:
                print(f"{first_name} {last_name} has made the Dean's List!")
            elif gpa >= 3.25:
                print(f"{first_name} {last_name} has made the Honor Roll.")
            else:
                print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")
        except ValueError:
            print("Invalid input for GPA. Please enter a numeric value.")

if __name__ == "__main__":
    main()
