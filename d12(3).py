def manage_marks():
    try:
        m1=float(input("Enter Subject 1 mark :"))
        m2=float(input("Enter Subject 2 mark :"))
        m3=float(input("Enter Subject 3 mark :"))
        m4=float(input("Enter Subject 4 mark :"))
        m5=float(input("Enter Subject 5 mark :"))
        marks=[m1,m2,m3,m4,m5]
        print("Marks :",marks)
        print("Average :",sum(marks)/len(marks))
        print("Highest :",max(marks))
        print("Highest :",min(marks))
        marks.sort(reverse=True)
        print("Descending Order :",marks)
    except ValueError:
        print("Invalid Input..!Enter numbers only.")
manage_marks()