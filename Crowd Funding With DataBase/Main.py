import Regstir,Mydata,login,project
from tabulate import tabulate
from datetime import datetime
import os

print("* Hello This is Authentication_System *")
x = input("** If you want to add users press y or Y ** ,** if you want to login enter L or l ** and ** if you want to exit enter E or e ** : ")
os.system('cls' if os.name == 'nt' else 'clear')
if x == 'y' or x == 'Y':
    while True:
        
        print("** This is adding user page **")
        #this to take data from user :
        
        # The ID first
        ID = Mydata.ID()
        ID = ID[0]+1
        
        flag1 = Regstir.ID(ID)
        # Then the fname and lname
        fname = input("please enter your first name: ")
        lname = input("please enter your last name: ")
        flag2 = Regstir.names(fname,lname)
        if not flag2:
            
            print("please enter a valid name")
            
            continue

        # The email 
        email = input("please enter your email: ")
        flag3 = Regstir.email(email)
        if not flag3:
            
            print("please enter a valid email")
            
            continue


        # The password
        password = input("please enter your password:  ")
        confirm = input("please confirm your password:  ")
        if confirm == password: 
            flag4 = Regstir.passw(password)
        else:
            while confirm != password:
                confirm = input("please confirm your password correctly: ")
                if confirm == password:
                    flag4 = Regstir.passw(password)
        if not flag4:
            
            print("please enter a right password should include one upper case and lower and one number at least ")
            
            continue


        # The phone
        mob = input("please enter your mobil number: ")
        row = Regstir.phone(mob)

        if not row:
           
            print("print please enter a valid egyptian number begin with 01")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            Mydata.add_row(row)
            


        # this section to break : 
        x = input("If you want to add another row press Y or y if you want to login enter L or l and if you want to exit enter E or e: ")
        
       
        if x == 'e' or x=='E':
            print("Thanks Sir")
            break
        elif x == 'l' or x =='L':
            break


# The Page of login and project


if x == 'L' or x=='l':
    
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Hello to LOGIN page")
        email = input("please enter your email: ")
        passw = input("please enter your password: ")

        usr= login.login(email,passw)
        while True:
            if usr:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(usr[0][0])
                print("""                     * if you want to show your project enter M or m *
                            * if you want to add project and mange it enter a or A *
                            * if you want to see whole projects enter w or W *
                            * if you want to delete your project enter d or D *
                            * if you want to update your project info enter u or U *
                            * if you want to searh by start date of the project enter S or s *
                            * if you want to serch by end date or the project enter e or E *
                            : 
                        """)
                a = input()

                if a == 'm' or a == 'M':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Your choice is M (show your project)")
                    proj = project.proj_manger(email,passw) 
                    print(tabulate(proj, headers=["Title","Details ","Total_target","Start_date","End_date","Manger"], tablefmt="grid"))
                elif a == 'a' or a == 'A':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Your choice is A (Adding project)")
                    title = input("please enter your project title: ")
                    detalis = input("please enter your project details: ")
                    tot = input("please enter your total target: ")
                    stdate = input("please enter the date of the start date in the format YYYY-MM-DD: ")
                    endate = input("please enter the date of the end date in the format YYYY-MM-DD: ")
                    
                    try:
                
                        stdate = datetime.strptime(stdate, "%Y-%m-%d").date()
                        endate = datetime.strptime(endate, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                    if endate > stdate:
                        flag1= project.add_proj(title,detalis,tot,stdate,endate,usr[0][0])
                        if flag1:
                            print("project added to you")
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("please enter a valid information")
                            continue
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("The end date should bigger than start date")
                        continue

                elif a == 'w' or a=='W':
                    proj=project.show_all()
                    print(tabulate(proj, headers=["Title","Details ","Total_target","Start_date","End_date","Manger"], tablefmt="grid"))
                elif a == 'd'or a == 'D':
                    title = input("enter your project title: ")
                    project.delete_proj(title)
                    print("deleted succsefully")
                elif a == 'u' or a == 'U':
                    title = input("please enter your project title: ")
                    detalis = input("please enter your project details: ")
                    tot = input("please enter your total target: ")
                    stdate = input("please enter the date of the start date in the format YYYY-MM-DD: ")
                    endate = input("please enter the date of the end date in the format YYYY-MM-DD: ")
                    
                    try:
                
                        stdate = datetime.strptime(stdate, "%Y-%m-%d").date()
                        endate = datetime.strptime(endate, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                    if endate > stdate:
                        flag1= project.edit_proj(title,detalis,tot,stdate,endate,title)
                        if flag1:
                            print("project added to you")
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("please enter a valid information")
                            continue
                elif a =='s' or a =='S':
                    stdate = input("please enter the date of the end date in the format YYYY-MM-DD: ")
                    
                    try:
                
                        stdate = datetime.strptime(stdate, "%Y-%m-%d").date()
                        proj = project.search_stdate(stdate)
                        print(tabulate(proj, headers=["Title","Details ","Total_target","Start_date","End_date","Manger"], tablefmt="grid"))
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                elif a =='e' or a =='E':
                    endate = input("please enter the date of the end date in the format YYYY-MM-DD: ")
                    
                    try:
                
                        endate = datetime.strptime(endate, "%Y-%m-%d").date()
                        proj = project.search_endate(endate)
                        print(tabulate(proj, headers=["Title","Details ","Total_target","Start_date","End_date","Manger"], tablefmt="grid"))

                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                else:
                    print(tabulate(usr, headers=["ID","First name","Last name","Phone","Projects",], tablefmt="grid"))
                
                x = input("If you finsh your work and want to exit enter e or E and if you want tontinue press any other key: ")
                if x =='e'or x=='E':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Thank You")
                    break


    
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid Email or Passowrd try again")
                continue
    

