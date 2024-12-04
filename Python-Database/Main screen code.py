#Main
import Deletemod
import Display_screen
import Insertmod
import Updatemod
import Viewmod

Display_screen.dis()
p="A"
print('''-----------------------Management Login-----------------------''')
print("")
while p=="A":
    dum="Y"
    psw=input("Enter your password here: ")
    print()
    while dum=="Y":
        if psw=="adivya":
            print('''Choose from the following:
1) Recruitment
2) Faculty
3) Finance
4) Manufacturing''')
            print()
            m=int(input("Enter your choice: "))
            print()
            if m==1:                                                                      #Recruitment
                print('''Choose which task is to be executed:
1) View Records
-------------------------
2) Insert Records
-------------------------
3) Update Records
-------------------------
4) Delete Records
-------------------------''')
                print()
                h=int(input("Enter your choice: "))
                print()
                if h==1:                                                                  #viewing
                    print('''1) Profiles
2) Applications' Status
3) Vacant Positions''')
                    print()
                    c=int(input("Enter your choice: "))
                    print()
                    if c==1:
                        Viewmod.view1()
                        print()
                    elif c==2:
                        Viewmod.view2()
                        print()
                    elif c==3:
                        Viewmod.view3()
                        print()
                    else:
                        print("Wrong Input")
                        print()
                elif h==2:                            #insert                                    #inserting
                    print('''1) Profiles
2) Applications' Status
3) Vacant Positions''')
                    print()
                    c=int(input("Enter your choice here: "))
                    print()
                    if c==1:
                        Insertmod.insert1()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:
                        Insertmod.insert2()
                        print()
                        print("Executed!")
                        print()
                    elif c==3:
                        Insertmod.insert3()
                        print()
                        print("Executed!")
                        print()
                    else:
                        print("Wrong Input")
                        print()
                elif h==3:                             #update                                   #updating
                    print('''1) Profiles
2) Applications' Status
3) Vacant Positions''')
                    print()
                    c=int(input("Enter choice here: "))
                    print()
                    if c==1:
                        Updatemod.update1()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:    
                        Updatemod.update2()
                        print()
                        print("Executed!")
                        print()
                    elif c==3:
                        Updatemod.update3()
                        print()
                        print("Excuted!")
                        print()
                    else:
                        print("Wrong input")
                        print()
                elif h==4:                             #delete                                   #deleting
                    print('''1) Profiles
2) Applications' Status
3) Vacant Positions''')
                    print()
                    c=int(input("Enter choice here: "))
                    if c==1:
                        Deletemod.delete1()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:
                        Deletemod.delete2()
                        print()
                        print("Executed!")
                        print()
                    elif c==3:
                        Deletemod.delete3()
                        print()
                        print("Executed!")
                        print()
                    else:
                        print("Wrong input")
                        print()
                else:
                    print("Wrong Input!")
            elif m==2:                               #faculty
                print('''Choose which task is to be executed:
1) View Records
-------------------------
2) Insert Records
-------------------------
3) Update Records
-------------------------
4) Delete Records
-------------------------''')
                print()
                h=int(input("Enter your choice: "))
                print()
                if h==1:                               #view 
                    print('''1) Staff Count
2) Amenities''')
                    print()
                    c=int(input("enter your choice: "))
                    print()
                    if c==1:
                        Viewmod.view4()
                        print()
                    elif c==2:
                        Viewmod.view5()
                        print()
                    else:
                        print("Wrong input")
                        print()
                elif h==2:                             #insert 
                    print('''1) Staff Count
2) Amenities''')
                    print()
                    c=int(input("Enter your choice: "))
                    print()
                    if c==1:
                        Insertmod.insert4()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:
                        Insertmod.insert5()
                        print()
                        print("Executed!")
                        print()
                    else:
                            print("Wrong input")
                            print()
                elif h==3:                              #update
                    print('''1) Staff Count
2) Amenities''')
                    print()
                    c=int(input("Enter your choice: "))
                    print()
                    if c==1:
                        Updatemod.update4()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:
                        Updatemod.update5()
                        print()
                        print("Executed!")
                        print()
                    else:
                        print("Wrong input")
                        print()
                elif h==4:                              #deleting
                    print('''1) Staff Count
2) Amenities''')
                    print()
                    c=int(input("Enter your choice here: "))
                    print()
                    if c==1:
                        Deletemod.delete4()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:
                        Deletemod.delete5()
                        print()
                        print("Executed!")
                        print()
                    else:
                        print("Wrong input")
                        print()
                else:
                    print("Wrong Input!")
            elif m==3:                                  #finance
                print('''Choose which task is to be executed:
1) View Records
-------------------------
2) Insert Records
-------------------------
3) Update Records
-------------------------
4) Delete Records
-------------------------''')
                print()
                h=int(input("Enter your chcoice: "))
                print()
                if h==1:                                #viewing
                    print('''1) Business Partners
2) Loans
3) Individual investors''')
                    print()
                    c=int(input("Enter choice here: "))
                    print()
                    if c==1:
                        Viewmod.view6()
                        print()
                    elif c==2:
                        Viewmod.view7()
                        print()
                    elif c==3:
                        Viewmod.view8()
                        print()
                    else:
                        print("Wrong input")
                        print()
                elif h==2:                              #inserting
                    print('''1) Business Partners
2) Loans
3) Individual investors''')
                    print()
                    c=int(input("Enter choice here: "))
                    print()
                    if c==1:
                        Insertmod.insert6()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:
                        Insertmod.insert7()
                        print()
                        print("Executed!")
                        print()
                    elif c==3:
                        Insertmod.insert8()
                        print()
                        print("Executed!")
                        print()
                    else:
                        print("Wrong input")
                        print()
                elif h==3:                              #updating
                    print('''1) Business Partners
2) Loans
3) Individual investors''')
                    print()
                    c=int(input("Enter your choice: "))
                    print()
                    if c==1:
                        Updatemod.update6()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:
                        Updatemod.update7()
                        print()
                        print("Executed!")
                        print()
                    elif c==3:
                        Updatemod.update8()
                        print()
                        print("Executed!")
                        print()
                    else:
                        print("Wrong input")
                        print()
                elif h==4:                              #deleting
                    print('''1) Business Partners
2) Loans
3) Individual investors''')
                    print()
                    c=int(input("Enter your choice: "))
                    print()
                    if c==1:
                        Deletemod.delete6()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:
                        Deletemod.delete7()
                        print()
                        print("Executed!")
                        print()
                    elif c==3:
                        Deletemod.delete8()
                        print()
                        print("Executed!")
                        print()
                    else:
                        print("Wrong input")
                        print()
                else:
                    print("Wrong Input!")
            elif m==4:                                  #manufacturing
                print('''Choose which task is to be executed:
1) View Records
-------------------------
2) Insert Records
-------------------------
3) Update Records
-------------------------
4) Delete Records
-------------------------''')
                print()
                h=int(input("Enter your choice: "))
                print()
                if h==1:                                #viewing
                    print('''1) Orders
2) Production Rate Statistics''')
                    print()
                    c=int(input("Enter your choice: "))
                    print()
                    if c==1:
                        Viewmod.view9()
                        print()
                    elif c==2:
                        Viewmod.view10()
                        print()
                    else:
                        print("Wrong Input")
                        print()
                elif h==2:                              #inserting
                    print('''1) Orders
2) Production Rate Statistics''')
                    print()
                    c=int(input("Enter your choice: "))
                    print()
                    if c==1:
                        Insertmod.insert9()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:
                        Insertmod.insert10()
                        print()
                        print("Executed!")
                        print()
                    else:
                        print("Wrong input")
                        print()
                elif h==3:                              #updating
                    print('''1) Orders
2) Production Rate Statistics''')
                    print()
                    c=int(input("Enter your choice: "))
                    print()
                    if c==1:
                        Updatemod.update9()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:
                        Updatemod.update10()
                        print()
                        print("Executed!")
                        print()
                    else:
                        print("Wrong input")
                        print()
                elif h==4:
                    print('''1) Orders
2) Production Rate Statistics''')
                    print()
                    c=int(input("Enter your choice here: "))
                    print()
                    if c==1:
                        Deletemod.delete9()
                        print()
                        print("Executed!")
                        print()
                    elif c==2:  
                        Deletemod.delete10()
                        print()
                        print("Executed!")
                        print()
                    else:
                        print("Wrong input")
                        print()
                else:
                    print("Wrong Input!")
            t=(input("Would you like to close the program?(Y/N): "))
            if t.upper()=="N":
                print()
                continue
            elif t.upper()=="Y":
                print()
                print("Have a nice day!")
                exit()
        else:                                   #wrong password!
            print("Wrong password!")
            print()
            y=input("Would you like to try again? (Y/N): ")             #to break the top most while loop and stop the process!
            if y.upper()=="Y":                          #yes
                p="A"
                print()
                break
            elif y.upper()=="N":                        #noo
                dum="B"
                exit()
