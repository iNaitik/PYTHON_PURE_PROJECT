import csv
file_name = "students.csv"
def load_data():
    student = []
    try:
        with open(file_name,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_dict = {
                    "RollNo": row["RollNo"],
                    "Name": row["Name"],
                    "Maths": int(row["Maths"]),
                    "Physics": int(row["Physics"]),
                    "Chemistry": int(row["Chemistry"])
                }
                student.append(student_dict)
    except(FileExistsError,FileNotFoundError):
        print("There is a problem in a file")
    return student

students = load_data()

def Subject_Average(students):
    temp1 = 0
    temp2 = 0
    temp3 = 0
    for row in students:
        temp1 = row['Maths'] + temp1
        temp2 = row['Physics'] + temp2
        temp3 = row['Chemistry'] + temp3
    count = len(students)
    if count == 0:
        print("No Student data")
        return
    Avg1 = float(temp1/count) 
    Avg2 = float(temp2/count) 
    Avg3 = float(temp3/count)

    print(f"Average marks in Maths: {Avg1:.2f}")
    print(f"Average marks in Physics: {Avg2:.2f}")
    print(f"Average marks in Chemistry: {Avg3:.2f}")

def student_totals_and_percentage(students):
    for row in students:
        Total = row['Maths'] + row['Physics'] + row ['Chemistry']
        Percentage = float(Total/300)*100
        print(f"ROll-NO: {row['RollNo']} || Name: {row['Name']} || Total: {Total} || Percentage: {Percentage:.2f}%")

def failed_students(students):
    failed = 0
    print("----FAILED STUDENTS----")
    for row in students:
        if (row['Maths'] < 40 or row['Physics'] < 40 or row['Chemistry'] < 40):
            print(f"Roll No: {row['RollNo']} || Name: {row['Name']} || Marks:- Maths:{row['Maths']}, Physics:{row['Physics']}, Chemistry:{row['Chemistry']}")
            failed += 1
    if failed == 0:
        print("NO STUDENT FAILED")
    else:
        print("--------------------")
        print(f"Total Students Failed: {failed}")

def rank_list(students):
    print("\nRANK LIST")
    print("---------")
    ranked = []
    for student in students:
        total = student['Maths'] + student['Physics'] + student['Chemistry']
        ranked.append({
            "RollNo": student['RollNo'],
            "Name": student['Name'],
            "Total": total
        })
    ranked.sort(key=lambda x: x['Total'], reverse=True)
    for i, student in enumerate(ranked):
        print(f"Rank {i+1} | Roll No: {student['RollNo']} | Name: {student['Name']} | Total Marks: {student['Total']}")
    print("---------")

def topper(students):
    if not students:
        print("No student data available.")
        return
    highest_total = 0
    for student in students:
        total = student['Maths'] + student['Physics'] + student['Chemistry']
        if total > highest_total:
            highest_total = total
    print("\nTOPPER(S) OF THE CLASS")
    print("---------------------")

    for student in students:
        total = student['Maths'] + student['Physics'] + student['Chemistry']
        if total == highest_total:
            print(f"Roll No: {student['RollNo']} | Name: {student['Name']} | Total Marks: {total}")
    print("---------------------")

if __name__ == "__main__":
    while True:
        print("\n--- Student Result Analyser ---")
        print("1. Subject-wise Average Marks")
        print("2. Student-wise Total and Percentage")
        print("3. List of Failed Students")
        print("4. Rank List")
        print("5. Topper of the Class")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            Subject_Average(students)
        elif choice == '2':
            student_totals_and_percentage(students)
        elif choice == '3':
            failed_students(students)
        elif choice == '4':
            rank_list(students)
        elif choice == '5':
            topper(students)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")