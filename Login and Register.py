import re
import csv

email_regex = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$')
pwd_regex = re.compile(r'^.*(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=.{5,}).*$')


def isValidEmail(email):
    if re.fullmatch(email_regex, email):
      return True
    else:
      return False

def isValidPwd(pwd):
    if len(pwd) < 16 and len(pwd) > 5 and re.fullmatch(pwd_regex, pwd):
      return True
    else:
      return False

def register():
    print('\nRegister New User\n')
    email = input('email id: ')
    if isValidEmail(email):
        password = input('password: ')
        if isValidPwd(password):
            write_file(email, password)
            print('\nUser Registered Successfully')
            print('''\n For Goto login select Option\n
                      1.yes
                      2.No
                      ''' )
            ans=int(input('option :'))
            if ans == 1 :
                login ()
            else:
                print('THANK YOU !!!')
                       
        else:
            print('\nInvalid Password, Please Try Again...')
    else:
        print('\nInvalid Username, Please Try Again...')

    

def login():
    email = input('email id: ')
    if isValidEmail(email):
        password = input('password: ')
        if isValidPwd(password):
            if search_file(email, password):
                print ('\nUser Logged In Successfully...')
            else:
                print('\nUser Not Found !!!')
                register()
        else:
            print('\nInvalid Password, Please Try Again...')
    else:
        print('\nInvalid Username, Please Try Again...')

def forget_pwd():
    email = input('email id: ')
    if isValidEmail(email):
        if search_pwd(email):
            print ('\nRemember your password...')
            print('''\n For Goto login select Option\n
                      1.yes
                      2.No
                      ''' )
            ans=int(input('option :'))
            if ans == 1 :
                login ()
            else:
                print('THANK YOU !!!')
        else:
            print('\nUser Not Found !!!')
            register()
    else:
        print('\nInvalid Username, Please Try Again...')

def search_file(email, pwd , mode = 'r', encoding = 'UTF8', newline = ''):
    with open('users.csv', mode, encoding = encoding, newline = newline) as f:
        reader = csv.reader(f)
        for row in reader:
            if email == row[0] and pwd == row[1]:
                return True
        return False

def search_pwd(email, mode = 'r', encoding = 'UTF8', newline = ''):
    with open('users.csv', mode, encoding = encoding, newline = newline) as f:
        reader = csv.reader(f)
        for row in reader:
            if email == row[0]:
                print('\nPassword for '+ email + ' is '+ row[1])
                return True
        return False
        

def write_file(email, pwd , mode = 'a', encoding = 'UTF8', newline = ''):
    with open('users.csv', mode, encoding = encoding, newline = newline) as f:
        writer = csv.writer(f)
        writer.writerow([email, pwd])

def home(option=None):
   
    try:
            print(''' \nPlease select an option \n
                1. Register
                2. Login
                3. Forget Password
                ''')
            option = int(input("option : "))
            if option == 1:
                register()
            elif option == 2:
                login()
            elif option == 3:
                forget_pwd()
            else:
                print("Invalid Option")
    except:
        print("An exception occurred")

home()

