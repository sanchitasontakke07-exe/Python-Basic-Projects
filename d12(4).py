class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.marks_list=[]
    def add_mark(self,mark):
        if 0 <= mark<= 100:
            self.marks_list.append(mark)
        else:
            print("Invalid Marks")
    def get_average(self):
        return sum(self.marks_list)/len(self.marks_list)
    def display_info(self):
        print("Name :",self.name)
        print("Roll No :",self.roll_no)
        print("Marks :",self.marks_list)
        print("Average:",self.get_average())
try:
    name=input("Enter Name :")
    roll= int(input("Enter Roll number :"))
    s=Student(name,roll)
    for i in range(3):
        mark=float(input("Enter Marks :"))
        s.add_mark(mark)
    s.display_info()
except ValueError:
        print("Invalid Input...!")