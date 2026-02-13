Student_Data = {
    101:{
        "name":"satya",
        "age":19,
        "marks":(19,20,20),
        "section":'A',
    },
    102:{
        "name":"shiva",
        "age":19,
        "marks":(15,14,20),
        "section":'B',
    }
}
while True:
    print("1.Add student")
    print("2.Display student")
    print("3.Search student")
    print("4.Remove student")
    print("5.Show class Topper")
    print("6.Display unique Section")
    print("7.Exit")
    choice = int(input("Enter(1-7):"))
    if choice == 1:
        try:
            Roll_no = int(input("Enter your Roll No:"))
            if Roll_no == "":
                print("Roll no cannot be empty")
            elif Roll_no in Student_Data:
                print("Roll no is already exist")
            else:
                name = input("enter your name:")
                age = int(input("enter your age:"))
                marks_list = []
                for i in range(1,4):
                    while True:
                        mark = int(input("enter marks:"))
                        if 0<= mark <= 20:
                            marks_list.append(mark)
                            break
                        else:
                            print("marks must be between 0-20:")
                marks = tuple(marks_list)

                section = input("enter your section").strip().upper()
                Student_Data[Roll_no] = {
                    "name":name,
                    "age":age,
                    "marks":marks,
                    "section":section
                }
                print("student added successfully!")
        except ValueError:
            print("Invalid input! please enter correct data")
    elif choice == 2:
        if not Student_Data:
            print("Student data is empty")
        else:
            print("student_details")
            for Roll_no,details in Student_Data.items():
                print("Roll no",Roll_no)
                print("name",details["name"])
                print("age",details["age"])
                print("marks",details["marks"])
                print("section",details["section"])
    elif choice == 3:
        try:
            Roll_no = int(input("enter your Roll no:"))
            if Roll_no in Student_Data:
                details = Student_Data[Roll_no]
                print("Roll no", Roll_no)
                print("name", details["name"])
                print("age", details["age"])
                print("marks", details["marks"])
                print("section", details["section"])
            else:
                print("student details not found")
        except ValueError:
            print("Invalid Roll no")
    elif choice == 4:
        try:
            Roll_no = int(input("enter your Roll no"))
            if Roll_no in Student_Data:
                del Student_Data[Roll_no]
                print("Roll no removed successfully")
            else:
                print("Roll no not Found")
        except ValueError:
            print("Invalid Roll no")
    elif choice == 5:
        if not Student_Data:
            print("Student Data is Empty")
        else:
            max_marks = 0
            topper_roll_no = None
            for Roll_no,details in Student_Data.items():
                total = sum(details["marks"])
                if total > max_marks:
                    max_marks = total
                    topper_roll_no = Roll_no
                    topper = Student_Data[topper_roll_no]
                    print("Roll no",topper_roll_no)
                    print("name",topper["name"])
                    print("total marks",max_marks)
    elif choice == 6:
        if not Student_Data:
            print("No student record found")
        else:
            sections = set()
            for details in Student_Data.values():
                sections.add(details["section"])
            print("unique sections:")
            for sec in sections:
                print(sec)
    elif choice == 7:
        print("Exiting Program....")
        break









