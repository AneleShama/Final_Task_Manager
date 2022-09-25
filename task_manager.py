 # References 1
 # I used L1T18 and L1T17 materials were very helpful to complete the task including it examples.

 # Reference 2
 # I used DevEnum.com
 # https://devenum.com/how-to-convert-text-file-to-a-dictionary-in-python/
 # I wanted to understand how I can store list of username and password

 # Reference 3
 # I used pythononthutorial 
 # https://www.pythontutorial.net/python-basics/python-write-text-file/
 # I have a problem with add to the file, when I was using 'w' if was created new file
 # Now I know I must use 'a' - append

 # Reference 4
 # Used programiz
 # https://www.programiz.com/python-programming/datetime/current-datetime
 # I wanted to know how to insert current date
 # I used this reference in new user section
 # I also used this reference to covert to a correct python format so that it can be read

 # Reference 5
 # I used GeeksforGeeks
 # https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
 # I wanted to understand how to check for certain value in a list
 # I now know I can simple use 'in' to check if something exist in the list
 # I used this reference in login section

 # Reference 6 
 # I used Stackoverflow
 # https://stackoverflow.com/questions/8865878/skipping-every-other-element-after-the-first
 # I wanted to learn how to create a list with certain sliced values
 # I know now that I can use [a::b] and simply specify the value of a and b - where I want slice alternate values
 # I used this reference in login section

 # Reference 7 
 # I used Stackoverflow 
 # https://stackoverflow.com/questions/8282553/removing-character-in-list-of-strings
 # I was struggling to remove a certain commas in the list 
 # I know now that I can use replace() funtion and loop over the list
 # I used this reference in login section
 # ========================================================

 #=====importing libraries===========

 # This line of code imports date from datetime modulus
from datetime import date
from datetime import datetime

 #=========== Register user =============
 # register menu will be deplayed if "r" is selected
def reg_user():                                         
    if username == "admin":  # Only admin have permission to add the new user
    
        user_name_info = ""  # create an empty string to read all stores usernames
        with open("user.txt", "r+") as user_name_detail:  # open user.txt for reading
            for line in user_name_detail:
                user_name_info  = user_name_info  + line  # this read all lines and store them in user_info variable

            user_name_list = list(user_name_info.strip().split())  # cating the user_info into a list
            user_info_name_list = [i.replace(',','') for i in user_name_list]  # this remove all ',' in all list items
            user_name = user_info_name_list[0::2]  # this create a list with all odd position items which is usernames in the user_info_list
            
        while True:
            new_user_ID = input("Enter the username:\n") # admin adds new user name
    
            if new_user_ID not in user_name:
                break  # if the user name is not found in the user.txt break to the next line of code
            elif new_user_ID in user_name:  # check if the username exist
                print(f"{new_user_ID} username is not available. Try another username")

 # This loop will continue until the password and it confirmation matches
 # new user will be added to user.txt file
 # by using append mode

        while True:
 # Admin adds username and password for the new user
            new_user_pass = input("Enter password:\n")  # admin adds pass for new user
            confirm = input("Confirm the password:\n")

 # Conditional statement, if the passwrod and
 # it confirmation matches
            if new_user_pass == confirm:
                print("\nNew user created successfully\n") 
 # append new user details to "user.txt" file
                with open('user.txt','a') as new_user:
                    new_user.write("\n" + str(new_user_ID) + ", " + str(new_user_pass))
                break 

            else:  # ask admin needs to enter passwords again until confirmed
                print("Passwords did not match. Try again")
    else:  # if user not an admin appropriate messange displayed
        print("You are not admin. Contact admin to add new user")

 #========== Add Task Section ========================= 
 # if 'a' is selected from menu, adding task is displayed
 # all information is added, once done append to tasks.txt file
def add_task():
 # the user need to insert all information on the task
    person = input("Username of the person given the task:\n")
    tittle = input("Enter the tittle of the task:\n")
    description = input("Enter the description of task:\n")
    due_date = input("Due date of the task in YYYY-MM-DD format:\n")
    date_now = date.today()  # This will input current live date
    completed = "No"

 # all the task attributes will be added to tasks.txt file
 # using append mode, the task will be wriiten to the tasks.txt
    with open("tasks.txt", "a") as new_task:
        new_task.write("\n" + str(person) + ", " + str(tittle) + ", " + str(description) + ", " + str(due_date) + ", " + str(date_now) + ", " + str(completed))

 #============ View All Section ================
 # User is able to read all task if 'va' is selected
 # all task in the task.txt file is displayed
def view_all_task():
    with open("tasks.txt", "r+") as view_all:  # open file in reading mode
        task_No = 0  # initializing task number in the task.txt

        for line in view_all:  # in the lines in view_all file, for loop reads lines in all tasks
            view_task = line.strip().split(", ")  # split the items in the tasks.txt where there is ", "
            person = view_task [0]   # this will slice item in index 0, which is the person a tasks is assined to
            tittle = view_task [1]   # this will slice item in index 1, which tasks tittle
            description = view_task[2]
            due_date = view_task [3]
            date_now = view_task [4]  # this date was automaticallt created using datetime modulus
            completed = view_task [5]
            task_No = task_No + 1
            print(f'''
Task No.\t{task_No}
Name:\t\t{person}
Tittle:\t\t{tittle}
Description:\t{description}
Due Date:\t{due_date}
Date created:\t{date_now}
Task Complete:\t{completed}
                ''')  # this prints out all task in user-friendly manner


 #============ View My task Section ================
 # This section is almost the same as View All Section
 # except that the logged in user only sees task assigned to them
def view_mine():
    task_ID = 1  # initializing task number in the task.txt
    my_task = []  # creating a temporary list for the current user
    
    with open("tasks.txt", "r+") as task_file_me:  # openning file for reading
        for row_num, line in enumerate(task_file_me):
            view_task = line.strip().split(", ")  # split the items in the tasks.txt where there is ", "
            person = view_task[0]  # this select users in task list, which is indent 0
            view_task.append(row_num)  # append the task nummber to my_task list
 # conditional to only show tasks
 # related to the logged in user
            if username == person:
                my_task.append(view_task)  # append task for current user in my_task list
    
    for i in my_task:
        print(f'''
Task Number:\t{task_ID}
Name:\t\t{i[0]}
Tittle:\t\t{i[1]}
Description:\t{i[2]}
Due Date:\t{i[3]}
Date created:\t{i[4]}
Task Complete:\t{i[5]}
                ''')  # this prints out logged in user task in user-friendly manner
        task_ID = task_ID + 1  # add one everytime we iterate in my_task list to obtain task number
 # ask user to select task number they want to edit
    task_num = int(input("Enter task number of you want to edit or '-1' to return to main menu:\t"))  
 # user select task number, if -1 or number greater that task number or negative interger,
 # the else statements will be execututed
    if task_num <= len(my_task) and task_num > 0:
        if task_num != -1:
            task = my_task[task_num - 1]  # if user select task 1 in my_task which is in equal index 0 in the my_task list
 # conditional for edit or mark as complete
            edit_option = input('''
Would you like to:
            e - edit task
            c - mark complete:\t''')

 # conditional for edit task
            if edit_option.lower() == 'e':
                    if task[5].lower() == "no":  # user cannot update if complete is == yes
                        edit = input('''
What you like to change:
            u - username
            d - due date:\t:''')

                        if edit.lower() == "u":  # if the user select u allow them to change username
                            task[0] = input("Please input new user:\t")
                        elif edit.lower() == "d":  # if the user enters somthing else, redirect them to main menu 
                            task[3] = input("Please new due date in YYYY-MM-dd format:\t")
                        else:  # if the user enters somthing else, redirect them to main menu  
                            print("Incorrect option")
                            main_manu()
                    else:
                        print("You cannot change this task, it has been completed")

            elif edit_option.lower() == "c":  # if the user select c allow them mark task complete
                task[5] = input("Is this task completed? 'Yes' or 'No':\t")
            else:   # if the user select somthing else, redirect them to main menu 
                print("Incorrect option")
                main_manu()
            
 # Updating the task.txt file to apply users changes
            index_position = task[6]  # Obtain indent number for the task at hand
            task = [str(i) for i in task]  # convert all intergers in the list to make them intergers
            task.pop()  # remove indent number in my_task list since we don't need it in task.txt
            updated_task = ', '.join(task)
            replace_content = ""
            i = 0  # initialize index number to get indent number of task in 'line' list

            with open('tasks.txt','r+') as file:  # open tasks.txt for reading
                for line in file:
                    line = line.strip()

 # is the line in 'line' list matches index number for task at hand,  
 # replace that line with an updated task
                    if i == index_position: 
                        new_line = line.replace(line, updated_task)
                    else:
                        new_line = line

                    replace_content = replace_content + new_line + "\n"
                    i = i + 1 
            
            with open('tasks.txt', 'w') as write_file:  # write to file to update the changes
                write_file.write(replace_content)  # this will always replace task.txt file
 # if the user select '-1' take them to main menu
    elif task_num == -1:
        main_manu()
 # if the user enters somthing number less than -1, redirect them to main menu 
    elif task_num < -1:
        print("Incorrect option")
        main_manu()
    else:
        print(f"You do not have task number {task_num}")
        main_manu()

 # =========== Reports Section ==============
 # this section generates reports, task_overview and user_overview
 # task_overview contains statistic about all task in the task manager application
 # user_overview contains statistic about users in the task manager application

def reports():

 # ============= task overview ==============
 # initializing necessary counts
    tot_task = 0
    tot_completed = 0
    tot_uncompleted = 0
    overdue_task = 0
    num_user = 0

    with open("tasks.txt", "r+") as task_overview:  # open task.txt file for reading
        for line in task_overview:
            view_task = line.strip().split(", ")  # split the items in the tasks.txt where there is ", "
            tot_task = tot_task + 1  # count the number of task every line we iterate
            
            task_completed = view_task[5]  # obtain value on weather task is complte or not

            if task_completed.lower() == "yes":  # if task complete is 'yes', count it every iteration
                tot_completed = tot_completed + 1
            elif task_completed.lower() == "no":   # if task complete is 'no', count it every iteration
                tot_uncompleted = tot_uncompleted + 1
            
            my_date = datetime.strptime(view_task[3], '%Y-%m-%d').date()  # convert date to python date format
 # if task date is less than today's date, task is overdue
            if my_date < date.today() and task_completed == "No":  
                overdue_task = overdue_task + 1  # count all overdue tasks

        percentage_incomplete = round((tot_completed * 100) / (tot_task),2)  # calculate % of incomplete task
        percentage_overdue = round((overdue_task * 100) / (tot_task),2)  # calculate % of incomplete task

    with open("task_overview.txt", "w") as write_overview:  # write to task_overview in user-friendly manner
        write_overview.write(f'''
Total number of tasks generated using Task Manager:     {tot_task}
Number of completed tasks:                              {tot_completed}
Number of uncompleted tasks:                            {tot_uncompleted}
Number of uncompleted tasks that are overdue:           {overdue_task}
Percentage of uncompleted tasks:                        {percentage_incomplete}%
Percentage of uncompleted overdue tasks:                {percentage_overdue}%
        ''')

 # ============ user_overvew ============

    users = []  # empty list to store all users
    with open("user.txt", "r+") as user_statistics:  # openinng user.txt file for reading
        for line in user_statistics:  # loop in all the lines of user.txt
            user_details = line.strip().split(", ")
            user_name_info = user_details[0]  # obtain users
            users.append(user_name_info)  # append all users to users list
            num_user = num_user + 1  # count number of users i=every iterate of line
            
    all_task = []  #  empty list to store all tasks

    with open("tasks.txt", "r+") as task_overview:  # open task file for reading
        for line in task_overview:
            view_task = line.strip().split(", ")
            all_task.append(view_task)  # append all task to all_task list

    with open("user_overview.txt", "w") as write_user_overview:  # write to user_overview file
        write_user_overview.write(
f'''
Total number of users                                   {num_user}
Total number of tasks generated using Task Manager:     {tot_task}     
        ''')

 # iterate in the user list and all task list at the same time
 # to find information related to each user
        for i in users:
 # initializing necessary counts
            user_task = 0
            user_complete = 0
            user_incomplete = 0
            user_overdue = 0
            
            for j in all_task:
 # if the user has a task and is completed, count the task and
 # count the completed task
                if i == j[0] and j[5].lower() == "yes":
                    user_task = user_task + 1
                    user_complete = user_complete + 1

 # if the user has a task and is not completed, and is overdue,
 # count the task and count the incompleted task
                elif i == j[0] and datetime.strptime(j[3], '%Y-%m-%d').date() < date.today():
                    user_task = user_task + 1
                    user_incomplete = user_incomplete + 1
                    user_overdue = user_overdue + 1

 # if the user has a task and is not completed, count the task and
 # count the incompleted task
                elif i == j[0] and j[5].lower() == "no":
                    user_task = user_task + 1
                    user_incomplete = user_incomplete + 1

 # if the user does not have a task all their statistic will be zero
                elif i != j[0]:
                    complete_percent = 0
                    incomplete_percent = 0
                    overdue_percent = 0

                task_percent = round((user_task / tot_task) * 100,2)  # calculate % of task each user have

                if user_task != 0:
                    complete_percent = round((user_complete / user_task) * 100,2)  # calculate % of completed task for each user
                    incomplete_percent = round((user_incomplete / user_task) * 100,2)  # calculate % of incompleted task for each user
                    overdue_percent = round((user_overdue / user_task) * 100,2)  # calculate % of overdue task for each user
 # write to user_overview.txt file
            write_user_overview.write(f'''
User:                         {i}
Number of user tasks          {user_task}
Percentage of total tasks     {task_percent}
Percentage completed          {complete_percent}
Percentage incomplete         {incomplete_percent}
Percentage overdue            {overdue_percent}
                    ''')    


 # =========== Statistic Section ==============
 # this section prints out the statistics to the admin
 # Only admin have these persmission
def statistics():
    if username == "admin": # check if the user is admin
 # it important that the admin get uodated information evertime 
 # he/she want to display statitcs
 # therefore we need to run report() function to obtain information 
 # from the file
        reports()  
        
        with open("task_overview.txt", "r+") as task_statistics:  # openinng tasks.txt for reading
            print("\nTASK OVERVIEW STATISTICS\n")
            for line in task_statistics: #  loop in all the lines of task.txt file
                print(line.strip())

        with open("user_overview.txt", "r+") as user_statistics:  # openinng user.txt file for reading
            print("\nUSER OVERVIEW STATISTICS\n")
            for line in user_statistics:  # loop in all the lines of user.txt
                print(line.strip())

 # if user is not admin - appropriate message displayed
    else:
        print("You not admin. You cannot view statistics\n")

 #=========== Exit Section ==========
 # Close the program if user enter 'e'
 # the program is killed using exit() function
def logout():
    print('Goodbye!!!')
    exit()

 #============= Menu Section ================
 # The user is presented with options after logged in 
 # Depending on the option the user select,
 # the user will be directed to that option
 # this will loop until the user exit the program by 
 # selecting 'e'

def main_manu():
    while True:
 # asking the user for there option
        menu = input('''Select one of the following Options below: 
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()

 # adding functions on user's selection
        if menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all_task()
        elif menu == 'vm':
            view_mine()
        elif menu == 'gr':
            reports()
        elif menu == 'ds':
            statistics()
        elif menu == 'e':
            logout()
        else:
            print("You have made a wrong choice, Please Try again\n")
        
 #====Login Section====
 # This section asks the user to enter their credentials
 # if the credentials matches with the ones in the list
 # the program gives user to the rest of the options
 # if not, the user is presented with an appropriate step to instruction

user_info = ""  # create an empty string to all stores user login infomation
with open("user.txt", "r+") as user_detail:  # open user.txt for reading
    for line in user_detail:
        user_info = user_info + line  # this read all lines and store them in user_info variable

    user_info_list = list(user_info.strip().split())  # cating the user_info into a list
    user_info_list = [i.replace(',','') for i in user_info_list]  # this remove all ',' in all list items
    user_name = user_info_list[0::2]  # this create a list with all odd position items which is usernames in the user_info_list
    user_pass = user_info_list[1::2]  # this create a list with all even position items which is passwords in the user_info_list

 # Until the user enters a password and username that matches
 # this will keep loop
 # the loop breaks if the user meet a required condition
    while True:
        username = input("Enter your username:\n")  # user enters username
        password = input("Enter your password:\n")  # user enters password

 # if the password and username are correct
 # the program breaks out the loop
        if username in user_name and password in user_pass:
            print("\nYou have successfully logged-in\n")
            main_manu()
 # if the password does not match with the username
 # an appropriate message is displayed
        elif username in user_name and password not in user_pass:
            print("\nThe password entered is incorrect. Try Again")
 # if the password and username are not found
 # 'user does not exist' is displayed
        else:
            print("\nThe user does not exist. Try again")
