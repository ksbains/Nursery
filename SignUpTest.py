import nursery
import main

def test1():
    #insert into the DB
    employeeName = "Karanbir Bains"
    employeeUsername = "ksbains"
    employeePassword = 'password'
    employeePhone_no = '4085556783'
    employeeStart = "2020-04-27"
    employeeJob = "Sales Associate"
    #Store 1 is San Jose location 
    employeeStoreID = 1
    #empId 1 is Lebron James manager fromt the start up script and already in the 
    employeeManager = 1
    #do the insert here
    nursery.insert_employee(employeeName, employeeUsername, employeePassword,employeeStoreID, employeeStart, employeePhone_no, employeeJob, employeeManager)
    employee = nursery.getEmployeeByName(employeeUsername, "emp_name")
    if employee == employeeName:
        print("Test 1 Passed!")
    else:
        print("Test 2 Failed!")

def test2():
    #insert into the DB
    employeeName = "Karanbir Bains"
    employeeUsername = "ksbains"
    employeePassword = 'password'
    employeePhone_no = '4085556783'
    employeeStart = "2020-04-27"
    employeeJob = "Sales Associate"
    #Store 1 is San Jose location 
    employeeStoreID = 1
    #empId 1 is Lebron James manager fromt the start up script and already in the 
    employeeManager = 1
    #do the insert here
    try:
        nursery.insert_employee(employeeName, employeeUsername, employeePassword,employeeStoreID, employeeStart, employeePhone_no, employeeJob, employeeManager)
        print("Test 2 Failed!")
    except Exception as e:
        # Error should occur here, no duplicates in the DB!!!!
        print("Test 2 Passed!")
    

def test3():
    customerName = "Karanbir Bains"
    customerUsername = "ksbains"
    customerPassword = 'password'
    customerPhone_no = '4085556783'
    customerAddress = "1 washington sq, San Jose CA 95148"
    customerEmail = "karanbir.bains@sjsu.edu"

    nursery.insert_customer(customerName, customerUsername, customerPassword, customerPhone_no, customerAddress, customerEmail)
    customer = nursery.getCustomerByName(customerUsername, "cust_name")
    if customer == customerName:
        print("Test 3 Passed!")
    else:
        print("Test 3 Failed!")


def test4():
    customerName = "Karanbir Bains"
    customerUsername = "ksbains"
    customerPassword = 'password'
    customerPhone_no = '4085556783'
    customerAddress = "1 washington sq, San Jose CA 95148"
    customerEmail = "karanbir.bains@sjsu.edu"

    try:
        nursery.insert_customer(customerName, customerUsername, customerPassword, customerPhone_no, customerAddress, customerEmail)
        print("Test 4 Failed!")
    except:
        # Error should occur here, no duplicates in the DB!!!!
        print("Test 4 Passed!")
def test5():
    empUsername = "ksbains"
    result = nursery.inEmployee(empUsername)
    if not result:
        print("Test 5 Failed!!")
    else:
        print("Test 5 Passed!!")

def test6():
    custUsername = "ksbains"
    result = nursery.inEmployee(custUsername)
    if not result:
        print("Test 6 Failed!!")
    else:
        print("Test 6 Passed!!")

def test7():
    #test if the password is the same hash that is in the DB for Employee
    EmployeeUsername = "ksbains"
    EmployeePassword = 'password'
    hashedPassword = nursery.getEmployeeByName(EmployeeUsername, "emp_password")
    valid = nursery.verify_password(hashedPassword, EmployeePassword) 
    if valid:
        print("Test 7 Passed!!")
    else:
        print("Test 7 Failed!!")

def test8():
    #test if the password is the same hash that is in the DB for Customer
    customerUsername = "ksbains"
    customerPassword = 'password'
    hashedPassword = nursery.getCustomerByName(customerUsername, "cust_password")
    valid = nursery.verify_password(hashedPassword, customerPassword)
    if valid:
        print("Test 8 Passed!!")
    else:
        print("Test 8 Failed!!")



    
def testScript():
    nursery.startup()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()




testScript()