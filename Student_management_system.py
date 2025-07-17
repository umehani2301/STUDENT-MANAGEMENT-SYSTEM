print("\n------WELCOME TO STUDENT MANAGEMENT SYSTEM------")

students = [{"roll no": 1, "Name":"Eva Roy","Branch":"AI and ML","Email Id":"evaroyy@gmail.com"},
            {"roll no": 2, "Name":"Aria Tavelry","Branch":"Computers","Email Id":"ariatavelryy@gmail.com"},
            {"roll no": 3, "Name":"Alex Volkov","Branch":"Mechanical","Email Id":"alexvolkovv@gmail.com"},
            {"roll no": 4, "Name":"Kai Azer","Branch":"Aeronautical","Email Id":"kaiazer@gmail.com"}]

while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Roll Number")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Exit")

    opt = int(input("\nEnter the number corresponding to your choice: "))

    if opt==1:
        print("\n------INFORMATION FOR ADDING A STUDENT------ ")
        roll = int(input("Enter the Roll No of the Student: "))
        name = input("Enter the Name of the Student: ")
        branch = input("Enter the branch of the Student: ")
        email = input("Enter the Email id of the Student: ")
        
        student = {"roll no": roll, "Name":name,"Branch":branch,"Email Id":email}
        students.append(student)

        print("\nStudent Added Successfully !")

    elif opt==2:
        print("\n------DISPLAYING ALL THE STUDENTS------ ")
        for i in students:
            print(i)
        
    elif opt==3:
        print("\n------SEARCHING FOR A STUDENT------ ")
        roll_to_search = int(input("Enter the roll no of the Student to search: "))
        
        found = False

        for student in students:
            if student["roll no"] == roll_to_search:
                print("\n Student found !")
                print("Name: ",student["Name"])
                print("Branch: ",student["Branch"])
                print("Email Id: ",student["Email Id"])

                found = True
                break
        if not found:
            print("\nNo student found with that roll no!")

    elif opt==4:
        print("\n------UPDATING STUDENT DETAILS------ ")
        
        roll_to_update = int(input("Enter the roll number of the student whose details are to upadted: "))

        updated = False

        for student in students:
            if student["roll no"] == roll_to_update:
                print(f"\n Fill in the following details for updating the details of [{roll_to_update}] roll number !")
                new_name = input("\nEnter the Name of the student:")
                new_branch = input("Enter the Branch of the student: ")
                new_email = input("Enter the Email id of the student: ")

                if new_name:
                    student["Name"] = new_name
                if new_branch:
                    student["Branch"] = new_branch
                if new_email:
                    student["Email Id"] = new_email

                print(f"Successfully updated the details of the roll number : {roll_to_update}")
                updated =  True
                break
        if not updated:
            print("No student found with that roll number !")

    elif opt==5:
        print("\n------DELETING THE DETAILS OF STUDENT------ ")

        roll_to_delete = int(input("Enter the roll no of the student whose details are to deleted: "))
        deleted = False

        for i in range(len(students)):
            if students[i]["roll no"] == roll_to_delete:
                del students[i]
                print("\nStudent Deleted Successfully !")
                deleted = True
                break
        if not deleted:
            print("\n No Student with that roll no is to be found !")
    
    elif opt==6:
        break

    else:
        print("\Invalid Option number selected !")
        print("Please Try Again !")

