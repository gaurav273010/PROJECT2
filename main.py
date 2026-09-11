print("WELCOME TO STUDENT DATA ORGANIZER !")

students=[]

while True:
    print("Please select an option")
    print("1. Add new student ")
    print("2. View all students ")
    print("3. update student information ")
    print("4. delete student ")
    print("5. display subjects offered ")
    print("6. exit")

    choice = input("enter your choice (1-6): ")

    if choice == "1":
        name = input("enter student name : ")
        age = int(input("enter student age : "))
        grade = input("enter student grade : ")
        id = int(input("enter student id : "))
        dob = input("enter student date of birth (YYYY-MM-DD)")
        subjects = input("enter student subjects (comma-seprarated):")

        information=(id,dob)
        subjects = set(subjects.split(","))

        student = {
            "Name": name ,
            "age" : age ,
            "grade":grade ,
            "subjects":subjects,
            "informations": information

            }
        students.append(student)
        print("new student added successfully.")

    elif choice =="2":
        if len(students)!=0:
            for std in students:
                print(f"student name is {std["Name"]}")
                print(f"student age is {std["age"]}")
                print(f"student grade is {std["grade"]}")
                print(f"student subject are {std["subjects"]}")
                print(f"student id is {std["informations"][0]}")
                print(f"student date of birth is {std["informations"][1]}")

        else:
            print("No data found")

    elif choice == "3":
        std_id = int(input("enter student id to update information: "))
        for std in students:
            if std["informations"][0] == std_id:
                print("student found")
                print("1. update name")
                print("2. update age")
                print("3. update grade")
                print("4. update subjects")

                update_choice = input("enter your choice (1-4): ")

                if update_choice == "1":
                    new_name = input("enter new name: ")
                    std["Name"] = new_name
                    print("name updated successfully.")

                elif update_choice == "2":
                    new_age = int(input("enter new age: "))
                    std["age"] = new_age
                    print("age updated successfully.")

                elif update_choice == "3":
                    new_grade = input("enter new grade: ")
                    std["grade"] = new_grade
                    print("grade updated successfully.")

                elif update_choice == "4":
                    new_subjects = input("enter new subjects (comma-separated): ")
                    std["subjects"] = set(new_subjects.split(","))
                    print("subjects updated successfully.")

                else:
                    print("invalid choice.")
                break
        else:
            print(f"student with id {std_id} not found.")
        
    
    elif choice == "4":
        std_id = int(input("enter student id to delete: "))
        for std in students:
            if std["informations"][0] == std_id:
                students.remove(std)
                print("student deleted successfully.")
                break
        else:
            print(f"student with id {std_id} not found.")

    elif choice == "5":
        subjects= set()
        for std in students:
            for sub in std["subjects"]:
                subjects.add(sub)
        print("subjects offered by students are:")
        for x in subjects:
            print(x)


    elif choice == "6":
        print("exit")
        break 