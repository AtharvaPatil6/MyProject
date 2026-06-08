students=[]

while True:
    print("Welcome To Student Marks Tracker")
    print("1.Add Student")
    print("2.View All Student")
    print("3.View Result")
    print("4.View Marks by Rollno.")
    print("5.To remove a student record.")
    print("6.Save Data To File")

    choice=int(input("Enter Your Choice(1/2/3/4/5/6): "))

    if choice==1:
        l=[]
        name=input("Add Student's Name: ")
        marks=int(input("Add Student's Marks: "))
        roll=int(input("Add Student's Rollno: "))
        l.append(marks)

        studentdict={
            "name":name,
            "marks":l,
            "rollno.":roll,
        }

        students.append(studentdict)

    elif choice==2:
        count=0
        for eachstudent in students:
            print(
                f"{count}--> {eachstudent['name']} "
                f"has marks: {eachstudent['marks']}, "
                f"rollno. {eachstudent['rollno.']}"
            )
            count+=1

    elif choice == 3:
        for result in students:
            marks = result["marks"][0]

            if marks <= 38:
                status = "FAIL"
            else:
                status = "PASS"

            print(
                f"{result['name']} --> "
                f"Marks: {marks} --> "
                f"{status}"
            )

    elif choice==4:
        found=False
        r=int(input("Enter Roll no.: "))

        for eachmarks in students:
            if eachmarks["rollno."] == r:
                found=True

                marks = eachmarks["marks"][0]

                if marks <= 38:
                    status = "FAIL"
                else:
                    status = "PASS"

                print(
                    f"Name: {eachmarks['name']} --> "
                    f"Marks: {marks} --> "
                    f"Status: {status}"
                )

        if not found:
            print("Student Not Found!!")

    elif choice==5:
        found=False
        r=int(input("Enter Roll no. to delete: "))

        for student in students:
            if student["rollno."] == r:
                students.remove(student)
                found=True
                print("Student has been removed Successfully!!")
                break

        if not found:
            print("Student Doesn't Exist")

    elif choice==6:
        with open("studentdata.txt","w") as f:
            f.write(str(students))
            print("Data File Created Successfully!!")

    else:
        print("Invalid Choice!")
