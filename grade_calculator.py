
def calculate_grade(percentage, marks):
    if any(mark < 35 for mark in marks):
        return "Fail"

    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "E"


def get_marks(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("=" * 45)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 45)

    name = input("Enter student name: ")

    subjects = ["Tamil", "English", "Maths", "Science", "Computer"]
    marks = []

    print("\nEnter the subject marks:")

    for subject in subjects:
        mark = get_marks(subject)
        marks.append(mark)

    total = sum(marks)
    percentage = (total / 500) * 100

    grade = calculate_grade(percentage, marks)

    if grade == "Fail":
        result = "FAIL"
    else:
        result = "PASS"

    print("\n" + "=" * 45)
    print("             STUDENT RESULT")
    print("=" * 45)

    print("Student Name :", name)
    print("-" * 45)

    for subject, mark in zip(subjects, marks):
        print(f"{subject:<15}: {mark:.2f}")

    print("-" * 45)
    print(f"Total Marks   : {total:.2f} / 500")
    print(f"Percentage    : {percentage:.2f}%")
    print(f"Grade         : {grade}")
    print(f"Result        : {result}")

    print("=" * 45)
    print("       Thank you for using our program!")
    print("=" * 45)


if __name__ == "__main__":
    main()
