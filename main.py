import datetime 
import time
from assignment import *

while True:
    q = str(input("press and key to enter in institute management system or 'Q' for quit:"))
    if q.title()=="Q":
        print("thank you for using this program")
        break
    else:
        try:
            obj = Asignment()
            print("""Opration Option
            1 For Add Operation
            2 For Get Operation
            3 For Asignment Operation""")
            user_option= int(input("please select you operation from above list:"))
            if user_option == 1:
                choose = int(input("""
                Do You Want To Add Trainer or Trainee
                1 for Trainer
                2 for Trainee
                enter the option:"""))
                if choose==1:
                    name = str(input("enter the name:")).title()
                    tech = str(input("enter the technology name:")).title()
                    active = str(input("enter the status:"))
                    obj.add_trainner(name,tech,active)
                elif choose==2:
                    name = str(input("enter the name:")).title()
                    tech = str(input("enter the technology name:")).title()
                    date = datetime.datetime.today()
                    joining_date = date.strftime("%b/%d/%Y")
                    duration = int(input("enter the number of month for duration of course:"))
                    email = str(input("enter the email id:"))
                    active = str(input("enter the status:"))
                    obj.add_trainee(name,tech,joining_date,duration,email_id=email,active=active)
                    obj.group_creation_with_trainer(technology_name=tech)
            elif user_option==2:
                print("""
                Do you want Get Trainer or Trainee
                1 for Trainer
                2 for Trainee
                """) 
                choose_get = int(input("enter the option:"))
                if choose_get == 1:
                    print("Welcome to Trainer Section")
                    time.sleep(2)
                    print("""
                    Do you wnat to get trainer by 
                    1 for name
                    2 for id
                    3 for technogy
                    """)
                    choose_trainer = int(input("enter option:"))
                    if choose_trainer==1:
                        name = str(input("enter the trainer name:")).title()
                        print(obj.get_trainer_by_name(name))
                    elif choose_trainer==2:
                        trainer_id = int(input("enter the id:"))
                        print(obj.get_trainer_by_id(trainer_id))
                    elif choose_trainer == 3:
                        tech_name =  str(input("enter the technology  name:")).title()
                        print(obj.get_trainee_by_technology(tech_name))
                    else:
                        print("please choose the correct option")
                elif choose_get == 2:
                    choose_trainee = int(input("enter option:"))
                    if choose_trainee==1:
                        name = str(input("enter the trainer name:")).title()
                        print(obj.get_trainee_by_name(name))
                    elif choose_trainee==2:
                        trainer_id = int(input("enter the id:"))
                        print(obj.get_trainee_by_id(trainer_id))
                    elif choose_trainee == 3:
                        tech_name =  str(input("enter the technology  name:")).title()
                        print(obj.get_trainee_by_technology(tech_name))
                    else:
                        print("please choose the correct option")
                else:
                    print("choose the correct option")
            elif user_option==3:
                print("""
                please select the way of asingment
                1. Do you want to asing trainee any perticular trainer
                2. Do you want to asing trainee in round-robin algorithm
                """)
                choose= int(input("please select your option:"))
                if choose==1:
                    pass
                elif choose==2:
                    tech_name = str(input("Enter the name of technology:"))
                    obj.group_creation_with_trainer(technology_name=tech_name)
                else:
                    print("please choose correct option:")
        except:
            print("choose correct option somthing went wrong")



  

    
                



    
                    







