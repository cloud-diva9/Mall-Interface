import mysql.connector as my
mydb = my.connect(host = 'localhost', user = 'root', password = 'ADMIN', autocommit = True)
c = mydb.cursor()
print('''Menu:
1- To create new database
2- To use existing one.
3- To Create Table.
4- To add values
5- To see all the records
6- To update them''')
while True:
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

        tabme = input('Enter new Table name: ')
        n = int(input('How many columns do you want?: '))

        columns = []
        for i in range(n):
            col_name = input(f'Enter name of column {i+1}: ')
            col_type = input(f'Enter datatype of {col_name} (INT, VARCHAR(50), FLOAT, etc.): ')
            columns.append(f'{col_name} {col_type}')

        query = (f'CREATE TABLE {tabme} ({', '.join(columns)})')
        c.execute(query)
        print('Table created successfully!')

        c.close()
        mydb.close()


    elif ch == 4: 
        tb = input('Enter Table name to create: ')

        if tb.lower() == 'employees':
            while True:
                emp_id = input('Enter Employee ID: ')
                first_name = input('Enter First Name: ')
                last_name = input('Enter Last Name: ')
                role = input('Enter Role: ')
                shift = input('Enter Shift: ')
                contact = int(input('Enter Contact Number: '))
                store_id = input('Enter Store ID: ')

                query = f'''
                INSERT INTO Employee
                (Employee_id, First_nme, Last_nme, Role, Shift, Contact_nmbr, Store_id)
                VALUES({emp_id}, {first_name}, {last_name}, {role}, {shift}, {contact}, {store_id}) '''

                c.execute(query)

                ch = input('Want to enter more data (y/n): ')
                if ch.lower() == 'n':
                    break

        elif tb.lower() == 'stores':
            while True:
                ##For store table
                category = input('Enter Category: ')
                floor = int(input('Enter Floor Level: '))
                unit = int(input('Enter Unit Number: '))
                lease_start = input('Enter Lease Start Date (YYYY-MM-DD): ')
                lease_end = input('Enter Lease End Date (YYYY-MM-DD): ')
                rent = int(input('Enter Rent Amount: '))
                contact_person = input('Enter Contact Person: ')
                contact = int(input('Enter Contact Number: '))


                query = f''' INSERT INTO YourTableName(Category, Floor_lvl, Unit_nmbr, Lease_start, Lease_end, Rent_amt, Contact_person, Contact_nmbr) 
                VALUES ('{category}', {floor}, {unit}, '{lease_start}', '{lease_end}', {rent}, '{contact_person}', {contact})'''
                
                c.execute(query)

                cho = input('Want to add more data (y/n)?: ')
                if cho.lower() == 'n':
                    break

        elif tb.lower() == 'behavior_analysis':
            while True:
                customer_id = input('Enter Customer ID: ')
                gender = input('Enter Gender: ')
                age = int(input('Enter Age: '))
                annual_income = int(input('Enter Annual Income (in k$): '))
                spending_score = int(input('Enter Spending Score (1-100): '))
                city = input('Enter City: ')
                purchase_history = input('Enter Purchase History/Frequency: ')
                payment_method = input('Enter Payment Method: ')
                traffic_source = input('Enter Traffic Source: ')
                cart_rate = float(input('Enter Cart Abandonment Rate (%): '))
                loyalty = input('Enter Loyalty Program Status: ')
                interests = input('Enter Interests/Hobbies: ')

                query = f'''
                INSERT INTO behavior_analysis VALUES
                ('{customer_id}', '{gender}', {age}, {annual_income}, {spending_score},
                '{city}', '{purchase_history}', '{payment_method}', '{traffic_source}',
                {cart_rate}, '{loyalty}', '{interests}')
                '''
                c.execute(query)

                cho = input('Want to add more data (y/n)?: ')
                if cho.lower() == 'n':
                    break

        else:
            print('Tha Table does\'nt exists!')


    elif ch == 5:
        tb = input('Enter the table name: ')
        if tb.lower() == 'stores':
            rec = c.execute('SELECT * FROM {tb}')

            for rec in c.fetchall():
                print(rec)

        elif tb.lower() == 'employees':
            rec = c.execute('SELECT * FROM {tb}')

            for rec in c.fetchall():
                print(rec)


        elif tb.lower() == 'behavior_analysis':
            rec = c.execute('SELECT * FROM {tb}')
            
            for rec in c.fetchall():
                print(rec)


    elif ch == 6:
        tb = input('Enter table name to update/delete the data: ')

        if tb.lower() == 'behavior_analytics':
            wh = input('Want to update or delete?: ')
            if wh.lower() == 'update':
                print('''What do you want to update?"
                1. Gender
                2. Age
                3. Annual Income
                4. Spending Score
                5. City
                6. Purchase History
                7. Payment Method
                8. Traffic Source
                9. Cart Abandonment Rate
                10. Loyalty Program Status
                11. Interests/Hobbies''')

                c_id = input("Enter CustomerID of the record to update: ")
                field_ch = int(input("Enter your choice: "))
                fields = {1: "Gender", 2: "Age", 3: "Annual_Income", 4: "Spending_Score", 5: "City",\
                        6: "Purchase_History", 7: "Payment_Method", 8: "Traffic_Source", 9: "Cart_Abandonment_Rate",\
                        10: "Loyalty_Program_Status",11: "Interests_Hobbies"}

                if field_ch in fields:
                    field = fields[field_ch]
                    if field in ['Age', 'Annual_Income', 'Spending_Score']:
                        new_value = int(input("Enter the new value: "))
                        query = f"UPDATE behavior_analysis SET {field} = {new_value}' WHERE CustomerID = '{c_id}'"
                        c.execute(query)
                        print("Record updated successfully!")

                    elif field == 'Cart_Abandonment_Rate':
                        new_value = float(input("Enter the new value: "))
                        query = f"UPDATE behavior_analysis SET {field} = {new_value}' WHERE CustomerID = '{c_id}'"
                        c.execute(query)
                        print("Record updated successfully!")

                    else:
                        new_value = input("Enter the new value: ")
                        query = f"UPDATE behavior_analysis SET {field} = {new_value}' WHERE CustomerID = '{c_id}'"
                        c.execute(query)
                        print("Record updated successfully!") 


                else:
                    print("Invalid choice.")

            elif wh.lower() == 'delete':
                customer_id = input("Enter CustomerID of the record to delete: ")
                query = f"DELETE FROM behavior_analysis WHERE CustomerID = '{customer_id}'"
                c.execute(query)
                print("Record deleted successfully!")

            else:
                print("Invalid choice.")


        elif tb == 'employees':
            wh = input('Want to update or delete?: ')
            if wh.lower() == 'update':
                print('''What do you want to update?"
                1. Gender
                2. Age
                3. Annual Income
                4. Spending Score
                5. City
                6. Purchase History
                7. Payment Method
                8. Traffic Source
                9. Cart Abandonment Rate
                10. Loyalty Program Status
                11. Interests/Hobbies''')

                c_id = input("Enter CustomerID of the record to update: ")
                field_ch = int(input("Enter your choice: "))
                fields = {1: "Gender", 2: "Age", 3: "Annual_Income", 4: "Spending_Score", 5: "City",\
                        6: "Purchase_History", 7: "Payment_Method", 8: "Traffic_Source", 9: "Cart_Abandonment_Rate",\
                        10: "Loyalty_Program_Status",11: "Interests_Hobbies"}

                if field_ch in fields:
                    field = fields[field_ch]
                    if field in ['Age', 'Annual_Income', 'Spending_Score']:
                        new_value = int(input("Enter the new value: "))
                        query = f"UPDATE behavior_analysis SET {field} = {new_value}' WHERE CustomerID = '{c_id}'"
                        c.execute(query)
                        print("Record updated successfully!")

                    elif field == 'Cart_Abandonment_Rate':
                        new_value = float(input("Enter the new value: "))
                        query = f"UPDATE behavior_analysis SET {field} = {new_value}' WHERE CustomerID = '{c_id}'"
                        c.execute(query)
                        print("Record updated successfully!")

                    else:
                        new_value = input("Enter the new value: ")
                        query = f"UPDATE behavior_analysis SET {field} = {new_value}' WHERE CustomerID = '{c_id}'"
                        c.execute(query)
                        print("Record updated successfully!") 


                else:
                    print("Invalid choice.")

            elif wh.lower() == 'delete':
                customer_id = input("Enter CustomerID of the record to delete: ")
                query = f"DELETE FROM behavior_analysis WHERE CustomerID = '{customer_id}'"
                c.execute(query)
                print("Record deleted successfully!")

            else:
                print("Invalid choice.")
