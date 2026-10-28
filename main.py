from tasks import  show_tasks
import os
from dotenv import load_dotenv

load_dotenv()

name = input("please enter your name : ")
print("welcome ", name)

admin_mode = input("do you want to open admin mode? yes/no: ")


if admin_mode.lower() == "yes":
    password = input("enter admin password: ")

    if password == os.getenv("admin_pass"):
        print("admin mode activated")
    else:
        print("wrong password")

        
tasks = []
count = int(input("how many task do you want to add?: "))
for i in range(count):
    task = input("enter a task: ")
    tasks.append(task)

show_tasks(tasks)