def student_database():
    students = {}   # roll number as key
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                roll_no = input("Enter Roll Number: ")

                name = input("Enter Student Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students.update({
                    roll_no: {
                        "name": name,
                        "age": age,
                        "city": city
                    }
                })
                print("Student added successfully!")
            elif choice == 2:
                roll_no = input("Enter Roll Number to search: ")
                student = students.get(roll_no)
                if student:
                    print("\nStudent Details:")
                    print("Name:", student["name"])
                    print("Age:", student["age"])
                    print("City:", student["city"])
                else:
                    print("Student not found!")
            elif choice == 3:
                if students:
                    print("\nAll Students:")
                    for roll, details in students.items():
                        print("\nRoll No:", roll)
                        print("Name:", details["name"])
                        print("Age:", details["age"])
                        print("City:", details["city"])
                else:
                    print("No student records available.")
            elif choice == 4:
                print("Exiting Student Database...")
                break
            else:
                print("Invalid choice! Select between 1-4.")
        except ValueError:
            print("Invalid input! Please enter correct values.")
        except Exception as e:
            print("Error:", e)
student_database()