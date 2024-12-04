import mysql.connector
def insert1():
    Name=input("Enter name of Employee: ")
    E_Id=int(input("Enter employee id: "))
    DOB=int(input("Enter date of birth(ddmmyy): "))
    Gend=input("Enter gender(M/F/N): ")
    May=int(input("Enter year of hiring: "))
    mydb=mysql.connector.connect(user='root', passwd='Adivya', host='localhost',database='project')
    mycursor=mydb.cursor()
    l=[]
    sql="Select E_Id from profiles where Year=%d"
    try:
        mycursor.execute("INSERT INTO Profiles(Name, E_Id, DOB, Gender, Year) VALUES ( '%s' ,'%d', '%d', '%s', '%d')"%(Name, E_Id, DOB, Gend, May))
        mydb.commit()
        mycursor.execute(sql%(May))
        res=mycursor.fetchall()
        for i in res:
            l=l+[i]
        s=len(l)
        mycursor.execute("Update cnt set Count=%d where date=%d"% (s,May))
        mydb.commit()
    except Exception as a:
        print(a)
        mydb.rollback()
def insert2():
    Id=int(input("Enter applicant id: "))
    Name=input("Enter name of applicant: ")
    Status=input("Application status(Approved/Rejected/On hold :: A/R/O): ")
    mydb=mysql.connector.connect(user='root', passwd='Adivya', host='localhost',database='project')
    mycursor=mydb.cursor()
    try:
        mycursor.execute("INSERT INTO Applications(Id, Name, Status) VALUES ('%d' ,'%s' ,'%s')"%(Id,Name, Status))
        mydb.commit()
    except Exception as a:
        print(a)
        mydb.rollback()
def insert3():
    Pos=input("Enter position in the company: ")
    status=input("Enter status(Vacant(V) or Filled(F)): ")
    mydb=mysql.connector.connect(user='root', passwd='Adivya', host='localhost',database='project')
    mycursor=mydb.cursor()
    try:
        mycursor.execute("INSERT INTO Vacancy(Position, Status) VALUES ( '%s' ,'%s')"%(Pos, status))
        mydb.commit()
    except Exception as a:
        print(a)
        mydb.rollback()
def insert4():
    Date=int(input("Enter Year: "))
    count=int(input("Enter staff count: "))
    mydb=mysql.connector.connect(user='root', passwd='Adivya', host='localhost',database='project')
    mycursor=mydb.cursor()
    try:
        mycursor.execute("INSERT INTO Cnt(date, Count) VALUES ( '%d' ,'%d')"%(Date, count))
        mydb.commit()
    except Exception as a:
        print(a)
        mydb.rollback()
def insert5():
    issue_no=int(input("Enter issuing number: "))
    floor_no=int(input("Enter floor number: "))
    I_req=input("Enter item required: ")
    I_amnt=int(input("Enter amount of items required: "))
    issue_date=int(input("Enter issuing date: "))
    mydb=mysql.connector.connect(user='root', passwd='Adivya', host='localhost',database='project')
    mycursor=mydb.cursor()
    try:
        mycursor.execute("INSERT INTO Amenities(Issue_No,Floor_No,Item_Required,Item_Amount,Issuing_Date) VALUES ( '%d' ,'%d', '%s', '%d', '%d')"%(issue_no,floor_no,I_req,I_amnt, issue_date))
        mydb.commit()
    except Exception as a:
        print(a)
        mydb.rollback()
def insert6():
    C_name=input("Enter company name: ")
    P_split=int(input("Enter splitting percentage of profit: "))
    investment=int(input("Enter investment amount: "))
    mydb=mysql.connector.connect(user='root', passwd='Adivya', host='localhost',database='project')
    mycursor=mydb.cursor()
    try:
        mycursor.execute("INSERT INTO Partners(Company_name,Split_percent, Investments) VALUES ( '%s' ,'%d','%d')"%(C_name,P_split,investment))
        mydb.commit()
    except Exception as a:
        print(a)
        mydb.rollback()
def insert7():
    b_name=input("Enter bank name: ")
    due_date=int(input("Enter last date to submit money(ddmmyy): "))
    due_amnt=int(input("Enter amount to be submitted: "))
    mydb=mysql.connector.connect(user='root', passwd='Adivya', host='localhost',database='project')
    mycursor=mydb.cursor()
    try:
        mycursor.execute("INSERT INTO Loans(Bank, Due_date, Due_amnt) VALUES ( '%s' ,'%d', '%d')"%(b_name,due_date,due_amnt))
        mydb.commit()
    except Exception as a:
        print(a)
        mydb.rollback()
def insert8():
    I_name=input("Enter investor name: ")
    I_amnt=int(input("Enter investment amount: "))
    mydb=mysql.connector.connect(user='root', passwd='Adivya', host='localhost',database='project')
    mycursor=mydb.cursor()
    try:
        mycursor.execute("INSERT INTO Investors(Name, Amount) VALUES ( '%s' ,'%d')"%(I_name,I_amnt))
        mydb.commit()
    except Exception as a:
        print(a)
        mydb.rollback()
def insert9():
    O_number=int(input("Enter order number: "))
    O_item=input("Enter product required: ")
    O_amnt=int(input("Enter amount required: "))
    O_date=int(input("Enter date of ordering: "))
    due_date=int(input("Enter date of delivery: "))
    mydb=mysql.connector.connect(user='root', passwd='Adivya', host='localhost',database='project')
    mycursor=mydb.cursor()
    try:
        mycursor.execute("INSERT INTO Orders(Order_no, Item, Amount, Order_Date, Due_date)VALUES ( '%d' ,'%s','%d','%d','%d')"%(O_number,O_item,O_amnt,O_date,due_date))
        mydb.commit()
    except Exception as a:
        print(a)
        mydb.rollback()
def insert10():
    Year=int(input("Enter year: "))
    prod=int(input("Enter production amount: "))
    inc=int(input("Enter production increment percentage(%): "))
    mydb=mysql.connector.connect(user='root', passwd='Adivya', host='localhost',database='project')
    mycursor=mydb.cursor()
    try:
        mycursor.execute("INSERT INTO Statistics(Year, Production_Amnt, Increment_Percent) VALUES ( '%d' ,'%d','%d')"%(Year,prod,inc))
        mydb.commit()
    except Exception as a:
        print(a)
        mydb.rollback()
