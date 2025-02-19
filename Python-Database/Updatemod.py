#update module
import mysql.connector


def update1():
    E_Id=int(input("Enter Employee id: "))
    E_id2=int(input("Enter new Employee id(if no new value, enter old value): "))
    Name=input("Enter new Name(if no new value, enter old value): ")
    Dob=int(input("Enter new date of birth(if no new value, enter old value): "))
    Gend=input("Enter new value of Gender(M/F/N ; if no new value, enter old value): ")
    may=int(input("Enter new value of year of hiring(if no new value, enter old value): "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        mycursor.execute("Update Profiles set Name='%s', E_id=%d, DOB=%d, Gender='%s', Year=%d where E_Id=%d"%(Name,E_id2,Dob,Gend,may,E_Id))
        mydb.commit()
    except Exception as a:
        print(a)
def update2():
    Id=int(input("Enter applicant id: "))
    Id2=int(input("Enter new Applicant Id(if no new value, enter old value): "))
    Name=input("Enter new Name(if no new value, enter old value): ")
    Status=input("Enter new Status(A/R/O ; if no new value, enter old value): ")
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        mycursor.execute("Update Applications set Name='%s',Status='%s',Id=%d where Id=%d"% (Name,Status,Id2,Id))
        mydb.commit()
    except Exception as a:
        print(a)
def update3():
    Pos=input("Enter position in the company: ")
    Pos1=input("Enter altered value of position(if no new value, enter old value): ")
    status=input("Enter new Status(V/F ; if no new value, enter old value): ")
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        mycursor.execute("Update Vacancy set Status='%s', Position='%s' where Position='%s'"% (status,Pos1,Pos))
        mydb.commit()
    except Exception as a:
        print(a)
def update4():
    Date=int(input("Enter Year: "))
    Date1=int(input("Enter altered value of Year(if no new value, enter old value): "))
    count=int(input("Enter new Staff count(if no new value, enter old value): "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        mycursor.execute("Update Cnt set date=%d,Count=%d where Date=%d"% (Date1,count,Date))
        mydb.commit()
    except Exception as a:
        print(a)
def update5():
    issueno=int(input("Enter issue number: "))
    issueno1=int(input("Enter new issue number(if no new value, enter old value): "))
    floor_no=int(input("Enter new value of floor number(if no new value, enter old value): "))
    I_rqd=input("Enter altered value of item required(if no new value, enter old value): ")
    I_amnt=int(input("Enter new item amount(if no new value, enter old value): "))
    I_date=int(input("Enter new issuing date(if no new value, enter old value):"))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        mycursor.execute("Update Amenities set Issue_No=%d,Floor_No=%d,Item_Required='%s',Item_Amount=%d,Issuing_Date=%d where Issue_No=%d"% (issueno1,floor_no,I_rqd,I_amnt,I_date,issueno))
        mydb.commit()
    except Exception as a:
        print(a)
def update6():
    C_name=input("Enter name of company: ")
    C_name1=input("Enter altered name of company(if no new value, enter old value): ")
    P_split=int(input("Enter new profit split percentage(if no new value, enter old value): "))
    inv=int(input("Enter new value of investment done(if no new value, enter old value): "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        mycursor.execute("Update Partners set Company_name='%s',Split_percent=%d,Investments=%d where Company_name='%s'"% (C_name1,P_split,inv,C_name))
        mydb.commit()
    except Exception as a:
        print(a)
def update7():
    Bank=input("Enter name of bank: ")
    Bank1=input("Enter altered name of bank(if no new value, enter old value):")
    duedate=int(input("Enter new due date(ddmmyy; if no new value, enter old value): "))
    dueamnt=int(input("Enter new due amount(if no new value, enter old value): "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        mycursor.execute("Update loans set Bank='%s',Due_date=%d, Due_amnt=%d where Bank='%s'"% (Bank1,duedate,dueamnt,Bank))
        mydb.commit()
    except Exception as a:
        print(a)
def update8():
    I_name=input("Enter name of Investor: ")
    I_name1=input("Enter altered name of Investor(if no new value, enter old value): ")
    I_amnt=int(input("Enter new investment amount(if no new value, enter old value): "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        mycursor.execute("Update Investors set Name='%s',Amount=%d where Name='%s'"% (I_name1,I_amnt,I_name,))
        mydb.commit()
    except Exception as a:
        print(a)
def update9():
    O_no=int(input("Enter order number: "))
    O_no1=int(input("Enter new order number(if no new value, enter old value): "))
    O_amnt=int(input("Enter new amount ordered(if no new value, enter old value): "))
    O_Item=input("Enter new item name(if no new value, enter old value): ")
    O_date=int(input("Enter new order date(if no new value, enter old value): "))
    D_date=int(input("Enter new due date(if no new value, enter old value): "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        mycursor.execute("Update Orders set Order_no=%d,Item='%s',Amount=%d,Order_Date=%d,Due_date=%d where Order_no=%d"% (O_no1,O_Item,O_amnt,O_date,D_date,O_no))
        mydb.commit()
    except Exception as a:
        print(a)
def update10():
    Year=int(input("Enter year: "))
    Year1=int(input("Enter new value of year(if none, enter old value): "))
    prod=int(input("Enter new Production amount(if no new value, enter old value): "))
    inc=int(input("Enter new Increment percentage(if no new value, enter old value): "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        mycursor.execute("Update Statistics set Year=%d,Production_Amnt=%d,Increment_Percent=%d where Year=%d"% (prod,inc,Year))
        mydb.commit()
    except Exception as a:
        print (a)
