import mysql.connector as my
mydb = my.connect(host = 'localhost', user = 'root', password = 'ADMIN', autocommit = True)
c = mydb.cursor()
print('''Menu:
1- To create new database
2- To use existing one.
3- To Create Table.
4- To add values
4- To see all the records
5- To update them''')
ch = int(input('Enther choice: '))
if ch == 1:

    db = input('Enter name of database: ')
    try:
        c.execute(f'Create database {db}')
    except:
        print('Already created')

    c.close()
    mydb.close()

elif ch == 2:
    db = input('Enter name of database: ')
    try:
        c.execute(f'USE {db}')
    except:
        print('Database already in use!')

    c.close()
    mydb.close()
        

elif ch == 3:
    db = input('Enter name of database: ')
    try:
        c.execute(f'USE {db}')  
        print('Database in use')

    except:
        print('Database in use')

    tabme = input("Enter new Table name: ")
    n = int(input("How many columns do you want?: "))

    columns = []
    for i in range(n):
        col_name = input(f"Enter name of column {i+1}: ")
        col_type = input(f"Enter datatype of {col_name} (INT, VARCHAR(50), FLOAT, etc.): ")
        columns.append(f"{col_name} {col_type}")

    query = (f"CREATE TABLE {tabme} ({', '.join(columns)})")
    c.execute(query)
    print("Table created successfully!")

    c.close()
    mydb.close()


elif ch == 4: 

    db = input('Enter name of database: ')
    try:
        c.execute(f'USE {db}')  
        print('Database in use')

    except:
        print('Database in use')

    emp_id = input("Enter Employee ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    role = input("Enter Role: ")
    shift = input("Enter Shift: ")
    contact = int(input("Enter Contact Number: "))
    store_id = input("Enter Store ID: ")

    query = f'''
    INSERT INTO Employee
    (Employee_id, First_nme, Last_nme, Role, Shift, Contact_nmbr, Store_id)
    VALUES({emp_id}, {first_name}, {last_name}, {role}, {shift}, {contact}, {store_id}) '''

    c.execute(query)
    print("Employee record inserted successfully!")


##For store table
    category = input("Enter Category: ")
    floor = int(input("Enter Floor Level: "))
    unit = int(input("Enter Unit Number: "))
    lease_start = input("Enter Lease Start Date (YYYY-MM-DD): ")
    lease_end = input("Enter Lease End Date (YYYY-MM-DD): ")
    rent = int(input("Enter Rent Amount: "))
    contact_person = input("Enter Contact Person: ")
    contact = int(input("Enter Contact Number: "))


    query = f''' INSERT INTO YourTableName(Category, Floor_lvl, Unit_nmbr, Lease_start, Lease_end, Rent_amt, Contact_person, Contact_nmbr) 
    VALUES ('{category}', {floor}, {unit}, '{lease_start}', '{lease_end}', {rent}, '{contact_person}', {contact})'''
    
    c.execute(query)
    print("Record inserted successfully!")

    customer_id = input("Enter Customer ID: ")
    gender = input("Enter Gender: ")
    age = int(input("Enter Age: "))
    annual_income = int(input("Enter Annual Income (in k$): "))
    spending_score = int(input("Enter Spending Score (1-100): "))
    city = input("Enter City: ")
    purchase_history = input("Enter Purchase History/Frequency: ")
    payment_method = input("Enter Payment Method: ")
    traffic_source = input("Enter Traffic Source: ")
    cart_rate = float(input("Enter Cart Abandonment Rate (%): "))
    loyalty = input("Enter Loyalty Program Status: ")
    interests = input("Enter Interests/Hobbies: ")

    # SQL Query using f-string
    query = f"""
    INSERT INTO behavior_analysis
    (CustomerID, Gender, Age, Annual_Income, Spending_Score,
    City, Purchase_History, Payment_Method, Traffic_Source,
    Cart_Abandonment_Rate, Loyalty_Program_Status, Interests_Hobbies)

    VALUES
    ('{customer_id}', '{gender}', {age}, {annual_income}, {spending_score},
    '{city}', '{purchase_history}', '{payment_method}', '{traffic_source}',
    {cart_rate}, '{loyalty}', '{interests}')
    """

    c.execute(query)

    print("Record Inserted Successfully!")


            

            