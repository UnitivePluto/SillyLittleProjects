import mysql.connector
def delete1():
    x=int(input("Enter employee id to be deleted: "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        ans=input("Are you sure you want to delete the record(y/n): ")
        l=[]
        if ans=='y':
            mycursor.execute("Select Year from profiles where E_Id=%d"%(x))
            res=mycursor.fetchall()
            for i in res:
                m=i[0]
            mycursor.execute("delete from Profiles where E_Id=%d"%(x))
            mydb.commit()
            mycursor.execute("select E_Id from profiles where Year=%d"%(m))
            res1=mycursor.fetchall()
            for j in res1:
                l=l+[j]
            s=len(l)
            mycursor.execute("Update cnt set Count=%d where date=%d"% (s,m))
            mydb.commit()
    except Exception as e:
        print(e)
def delete2():
    x=int(input("Enter applicant id to be deleted: "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        ans=input("Are you sure you want to delete the record(y/n): ")
        if ans=='y':
            mycursor.execute("delete from Applications where Id=%d"%(x))
            mydb.commit()
    except Exception as e:
        print(e)
def delete3():
    x=input("Enter position to be deleted: ")
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        ans=input("Are you sure you want to delete the record(y/n): ")
        if ans=='y':
            mycursor.execute("delete from Vacancy where Position='%s'"%(x))
            mydb.commit()
    except Exception as e:
        print(e)
def delete4():
    x=int(input("Enter Year to be deleted: "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        ans=input("Are you sure you want to delete the record(y/n): ")
        if ans=='y':
            mycursor.execute("delete from Cnt where date=%d"%(x))
            mydb.commit()
    except Exception as e:
        print(e)
def delete5():
    x=int(input("Enter issue number: "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        ans=input("Are you sure you want to delete the record(y/n): ")
        if ans=='y':
            mycursor.execute("delete from Amenities where Issue_No=%d"%(x))
            mydb.commit()
    except Exception as e:
        print(e)
def delete6():
    x=input("Enter company name to be deleted: ")
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        ans=input("Are you sure you want to delete the record(y/n): ")
        if ans=='y':
            mycursor.execute("delete from Partners where Company_name='%s'"%(x))
            mydb.commit()
    except Exception as e:
        print(e)
def delete7():
    x=input("Enter bank name to be deleted: ")
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        ans=input("Are you sure you want to delete the record(y/n): ")
        if ans=='y':
            mycursor.execute("delete from Loans where Bank='%s'"%(x))
            mydb.commit()
    except Exception as e:
        print(e)
def delete8():
    x=input("Enter investor name to be deleted: ")
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        ans=input("Are you sure you want to delete the record(y/n): ")
        if ans=='y':
            mycursor.execute("delete from Investors where Name='%s'"%(x))
            mydb.commit()
    except Exception as e:
        print(e)
def delete9():
    x=int(input("Enter order number to be deleted: "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        ans=input("Are you sure you want to delete the record(y/n): ")
        if ans=='y':
            mycursor.execute("delete from Orders where Order_no=%d"%(x))
            mydb.commit()
    except Exception as e:
        print(e)
def delete10():
    x=int(input("Enter year to be deleted: "))
    try:
        mydb=mysql.connector.connect(user='root', password='Adivya', host='localhost',database='project')
        mycursor = mydb.cursor()
        ans=input("Are you sure you want to delete the record(y/n): ")
        if ans=='y':
            mycursor.execute("delete from Statistics where Year=%d"%(x))
            mydb.commit()
    except Exception as e:
        print(e)

