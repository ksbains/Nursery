import mysql.connector
import nursery
import inquirer
import ordersFlow
import trendingFlow
import nursery_store
import re
from pyfiglet import figlet_format
from prettytable import PrettyTable
from datetime import datetime



def getConnection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="nursery"
    )
    return conn

# Jasper's changes
def empManMenu(empID, storeID):
    questions = [inquirer.List('empManageOption',
                message="What would you like to do?",
                choices=['View Employees', 'Hire Employee', 'Fire Employee', 'Promote Employee', 'Back'])]
    answer    = inquirer.prompt(questions)['empManageOption']

    if answer == 'View Employees':
        viewEmployees(empID, storeID)
    elif answer == "Hire Employee":
        hireEmployee(empID, storeID)
    elif answer == "Fire Employee":
        fireEmployee(empID, storeID)
    elif answer == "Promote Employee":
        promoteEmployee(empID, storeID)
    else:
        employeeManagerMainMenu(empID, storeID)


# Jasper's changes
def viewEmployees(empID, storeID):
    employees   = nursery.getEmployees(storeID)
    columnNames = getColumnNames('employee')
    columnNames.pop(3)
    employeesExceptPw = []

    for emp in employees:
        temp = list(emp)
        temp.pop(3)
        employeesExceptPw.append(tuple(temp))
    showTabularResults(employeesExceptPw, columnNames, 30, 'Employee')

    questions = [inquirer.List('done',message="Press", choices=['Done'])]
    done      = inquirer.prompt(questions)['done']

    if done:
        empManMenu(empID, storeID)


# Jasper's changes
def hireEmployee(empID, storeID):

    # enter new hire information
    while True:
        questions = [inquirer.Text('name',       message="Enter employee name")]
        empName = inquirer.prompt(questions)['name']

        flag = False
        if not empName:
            msg = '\n[No entry for name]\n'
            flag = True
        elif re.search("[0-9]", empName):
            flag = True
            msg = '\n[Name cannot contain numbers]\n'

        if flag:
            print(msg)
            questions = [inquirer.List('select option',message="Choose", choices=['Re-enter', 'Cancel'])]
            answer    = inquirer.prompt(questions)['select option']

            if answer == 'Re-enter':
                continue
            else:
                empManMenu(empID, storeID)
        else:
            break

    while True:
        questions = [inquirer.Text('username',   message="Enter employee username")]
        empUserName = inquirer.prompt(questions)['username']

        flag = False
        if not empUserName:
            msg = '\n[No entry for username]\n'
            flag = True

        if flag:
            print(msg)
            questions = [inquirer.List('select option',message="Choose", choices=['Re-enter', 'Cancel'])]
            answer    = inquirer.prompt(questions)['select option']

            if answer == 'Re-enter':
                continue
            else:
                empManMenu(empID, storeID)
        else:
            break

    while True:
        questions = [inquirer.Text('password',   message="Enter employee password")]
        empPassword = inquirer.prompt(questions)['password']

        flag = False
        if not empPassword:
            msg = '\n[No entry for password]\n'
            flag = True

        if flag:
            print(msg)
            questions = [inquirer.List('select option',message="Choose", choices=['Re-enter', 'Cancel'])]
            answer    = inquirer.prompt(questions)['select option']

            if answer == 'Re-enter':
                continue
            else:
                empManMenu(empID, storeID)
        else:
            break

    while True:
        questions = [inquirer.Text('phone_no',   message="Enter employee phone number")]
        empPhone = inquirer.prompt(questions)['phone_no']

        flag = False
        if not empPhone:
            msg = '\n[No entry for phone number]\n'
            flag = True
        elif re.search('[a-zA-Z]', empPhone):
            msg = '\n[Phone number contains a letter]\n'
            flag = True

        if flag:
            print(msg)
            questions = [inquirer.List('select option',message="Choose", choices=['Re-enter', 'Cancel'])]
            answer    = inquirer.prompt(questions)['select option']

            if answer == 'Re-enter':
                continue
            else:
                empManMenu(empID, storeID)
        else:
            break

    while True:
        questions = [inquirer.Text('start_date', message="Enter employee start date (yyyy-mm-dd)")]
        empStartDate = inquirer.prompt(questions)['start_date']

        flag = False
        if not empStartDate:
            msg = '\n[No entry for start date]\n'
            flag = True
        elif not re.search('\d{4}[-\.\s]\d{1,2}[-\.\s]\d{1,2}', empStartDate):
            msg = '\n[Date format invalid]\n'
            flag = True
        else:
            empStartDate = re.sub(r'[\.\s]', '-', empStartDate)
            if not valiDate(empStartDate):
                msg = '\n[Date invalid]\n'
                flag = True

        if flag:
            print(msg)
            questions = [inquirer.List('select option',message="Choose", choices=['Re-enter', 'Cancel'])]
            answer    = inquirer.prompt(questions)['select option']

            if answer == 'Re-enter':
                continue
            else:
                empManMenu(empID, storeID)
        else:
            break

    questions   = [inquirer.List('job_title',  message='Select employee job title',choices=['Manager', 'Sales Associate'],default='Sales Associate')]
    empJobTitle = inquirer.prompt(questions)['job_title']
    empStoreID  = storeID
    empMngrID   = empID

    nursery.insert_employee(empName, empUserName, empPassword, empStoreID, empStartDate, empPhone, empJobTitle, empMngrID)
    print('\n[Employee successfully entered]\n')
    empManMenu(empID, storeID)


# Jasper's changes
# Option 1: Display employees in tabular format then
# prompt user to enter ID of employee for termination
# def fireEmployee(empID, storeID):
#
#     employees   = nursery.getEmployees(storeID)
#     columnNames = getColumnNames('employee')
#     columnNames.pop(3)
#     employeesExceptPw = []
#
#     for emp in employees:
#         temp = list(emp)
#         temp.pop(3)
#         employeesExceptPw.append(tuple(temp))
#     showTabularResults(employeesExceptPw, columnNames, 30, 'Employee')
#
#     questions  = [inquirer.Text('emp_id', message="Enter ID of employee to be fired")]
#     answers    = inquirer.prompt(questions)
#     employeeID = answers['emp_id']
#
#     if employeeID == empID:
#         print("Invalid Operation: Cannot fire selected employee")
#     else:
#         nursery.delete_employee(employeeID)
#
#     empManMenu(empID, storeID)


# Jasper's changes
# Option 2: Use checkbox to select employees for termination
def fireEmployee(empID, storeID):

    indexes         = [2, 3, 5, 6]
    employees       = nursery.getEmployees(storeID)
    employeesString = []
    empIDMapping    = {}

    # Store the following values for each employee as a string in employeesString:
    # emp_id, emp_name, store_id, designation, supervisor_id
    for emp in employees:
        if emp[0] ==  empID:
            continue
        temp = list(emp)
        temp = map(str, temp)
        for index in sorted(indexes, reverse=True):
            del temp[index]
        newString = ', '.join(temp)
        employeesString.append(newString)
        empIDMapping[newString] = emp[0]

    while True:
        questions = [inquirer.Checkbox('firees', message="Select employees for termination", choices=employeesString)]
        firees    = inquirer.prompt(questions)['firees']

        if not firees:
            print('\n[No employees selected]\n')
            questions = [inquirer.List('select option',message="Choose", choices=['Select again', 'Cancel'])]
            answer    = inquirer.prompt(questions)['select option']

            if answer == 'Select again':
                continue
            else:
                empManMenu(empID, storeID)
        else:
            questions = [inquirer.List('confirm',message="Select", choices=['Confirm', 'Cancel'])]
            confirm   = inquirer.prompt(questions)['confirm']

            if confirm == 'Confirm':
                for emp in firees:
                    nursery.delete_employee(empIDMapping[emp])
                print('\n[Successfully deleted]\n')
            empManMenu(empID, storeID)


# Jasper's changes
def promoteEmployee(empID, storeID):
    indexes         = [2, 3, 5, 6]
    employees       = nursery.getEmployees(storeID)
    employeesString = []
    empIDMapping    = {}

    # Store the following values for each employee as a string in employeesString:
    # emp_id, emp_name, store_id, designation, supervisor_id
    for emp in employees:
        if emp[0] ==  empID:
            continue
        temp = list(emp)
        temp = map(str, temp)
        for index in sorted(indexes, reverse=True):
            del temp[index]
        newString = ', '.join(temp)
        employeesString.append(newString)
        empIDMapping[newString] = emp[0]

    while True:
        questions = [inquirer.Checkbox('promotees', message="Select employees for promotion", choices=employeesString)]
        promotees = inquirer.prompt(questions)['promotees']

        if not promotees:
            print('\n[No employees selected]\n')
            questions = [inquirer.List('select option',message="Choose", choices=['Select again', 'Cancel'])]
            answer    = inquirer.prompt(questions)['select option']

            if answer == 'Select again':
                continue
            else:
                empManMenu(empID, storeID)
        else:
            questions = [inquirer.List('confirm',message="Select", choices=['Confirm', 'Cancel'])]
            confirm   = inquirer.prompt(questions)['confirm']

            if confirm == 'Confirm':
                for emp in promotees:
                    nursery.update_supID(empIDMapping[emp], None)
                print('\n[Successfully updated]\n')
            empManMenu(empID, storeID)

# Jasper's changes
def getColumnNames(table):
    conn     = getConnection()
    cursor   = conn.cursor()
    colNames = []
    sql      = "DESC {}".format(table)
    cursor.execute(sql)
    result   = cursor.fetchall()
    cursor.close()
    conn.close()

    for col in result:
        colNames.append(col[0])
    return colNames


# Jasper's changes
def showTabularResults(rows, columnNames, columnWidth, tableTitle):
    columnWidths = {}
    t            = PrettyTable(columnNames)
    t.title      = tableTitle
    t._max_width = columnWidths

    for col in columnNames:
        columnWidths[col] = columnWidth
    for row in rows:
        t.add_row(row)
    print(t)


# Jasper's changes
def valiDate(date):
    try:
        if date != datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False


empManMenu(3, 1)
