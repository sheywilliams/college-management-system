import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '1seunwilliams!' , database  = 'cms')
mycursor = mydb.cursor(buffered=True)

# mycursor.execute("CREATE DATABASE cms")
# mycursor.execute("SHOW DATABASES")
# for database in mycursor:
#     print(database)
# mycursor.execute('CREATE TABLE Users (id INT(7), username VARCHAR(255), password VARCHAR(255), priviledge VARCHAR(255))')
# mycursor.execute('ALTER TABLE Users MODIFY COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY')



def admin_session():
    print('Login success, welcome admin')
    while 1:
        print('')
        print('Admin menu')
        print('1. Register new student')
        print('2. Register new teacher')
        print('3. Delete existing student')
        print('4. Delete existing teacher')
        print('5. Logout')

        user_option = input(str('Option : '))
        if user_option == '1':
            print('')
            print('Register new student')
            username = input(str('Student username : '))
            password = input(str('Student password : '))
            query_vals = (username, password)
            mycursor.execute("INSERT INTO Users (username, password, priviledge) VALUES (%s, %s, 'student')", query_vals)
            mydb.commit()
            print(username + ' has been registered as student1 ')

            

def auth_admin():
    print('')
    print('Admin login')
    print('')
    username = input(str('username : '))
    password = input(str('password : '))
    if username == 'admin':
        if password == 'password':
            admin_session()
        else:
            print('Incorrect password')
    else:
        print('incorrect login details')            

def main():
    while 1:
        print('welcome to the college system')
        print('')
        print('1. Login as student')
        print('2. Login as teacher')
        print('3. Login as admin')

        user_option = input(str('Option: '))
        if user_option =='1':
            print('student login')
        elif user_option == '2':
            print('teacher login')
        elif user_option == '3':
          auth_admin()       
        else:
            print('No valid option')    
main()
