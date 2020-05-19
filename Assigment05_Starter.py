# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Zhihua Shang>,<5/18/2020>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

dataFile = open(objFile, 'r')
for row in dataFile:
    lstRow = row.split(',')
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip()}
    lstTable.append(dicRow)
dataFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input('Which option would you like to perform? [1 to 5] - '))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Task' + ':' + 'Priority')
        for dicRow in lstTable:
            print(dicRow['Task'] + ':' + dicRow['Priority'].strip())
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask = input('Enter your task that you want to add: ')
        newPriority = input('Enter your priority:')
        dicRow = {'Task': newTask, 'Priority': newPriority}
        lstTable.append(dicRow)
        print('\n', newTask, 'has been added.')
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        delTask = input('Enter your task that you want to remove: ')
        for dicRow in lstTable:
            if dicRow['Task'].lower() == delTask.lower():
                lstTable.remove(dicRow)
                print('\nOkay.', delTask, 'has been deleted.')
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        dataFile = open('ToDoToDoList.txt', 'w')
        for dicRow in lstTable:
            dataFile.write(dicRow['Task'] + ',' + dicRow['Priority']+'\n')
        dataFile.close()
        print("Saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        exitStr = input('Are you sure? If yes, type exit to end the program')
        if exitStr.lower() == 'exit':
            break  # and Exit the program
