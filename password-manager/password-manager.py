import base64
import mysql.connector as mc


# -- Authenticates user -----------------------------------------------------------
def user_authentication():
    exit_auth = 0
    authenticated = False
    saved_username = base64.b64encode(b'user')
    saved_password = base64.b64encode(b'password')

    while not exit_auth:
        main_username = input("Enter your username: ")
        main_password = input("Enter your password: ")

        if base64.b64encode(main_username.encode('ascii')) == saved_username and base64.b64encode(
                main_password.encode('ascii')) == saved_password:
            print("\n---------------User Authenticated Successfully---------------")
            authenticated = True
            exit_auth = 1

        else:
            continue_option = input(
                "\nAuthentication failed. Do you want to proceed with trying again? (y to approve and any "
                "character to reject): ")
            if continue_option.lower() == "y" or continue_option.lower() == "yes":
                exit_auth = 0
            else:
                print("\n---------------Bye!---------------")
                exit_auth = 1

    return authenticated


# -- Creates the database ----------------------------------------------------------
def create_database(mysql_root_password):
    print("\n---------------Checking Database---------------")
    password_database = mc.connect(
        host="localhost",
        user="root",
        password=mysql_root_password
    )
    password_cursor = password_database.cursor()
    password_cursor.execute("CREATE DATABASE IF NOT EXISTS password_manager")
    password_cursor.close()
    password_database.close()


# -- Connects to the MYSQL database using credentials ------------------------------
def connect_to_database(mysql_root_password):
    passwords_database = mc.connect(
        host="localhost",
        user="root",
        password=mysql_root_password,
        database="password_manager"
    )
    return passwords_database


def create_table(mysql_root_password):
    print("\n---------------Checking Table---------------")
    passwords_database = connect_to_database(mysql_root_password)
    passwords_cursor = passwords_database.cursor()
    passwords_cursor.execute(
        'CREATE TABLE IF NOT EXISTS passwords (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, UNIQUE (title))')

    passwords_cursor.close()
    passwords_database.close()
    return passwords_database


# -- Inserts new username/password to the database ---------------------------------
def insert_to_database(mysql_root_password, title, username, password):
    print("\n---------------Storing Username/Password---------------")
    passwords_database = connect_to_database(mysql_root_password)
    password_cursor = passwords_database.cursor()
    sql = "INSERT INTO passwords (title, username, password) VALUES (%s, %s, %s)"
    val = (title, username, password)
    password_cursor.execute(sql, val)
    passwords_database.commit()

    password_cursor.close()
    passwords_database.close()
    print(f"{'📗'} Credentials Stored.")


# -- Handles database with the new username/password -------------------------------
def new_password(mysql_root_password):
    print("\n---------------New Credentials---------------")
    title = input("\nEnter the title (website, OS, etc.): ")
    username = input("Enter the username you want to save: ")
    password = input("Enter the corresponding password: ")

    encoded_password = base64.b64encode(password.encode('ascii'))
    create_database(mysql_root_password)
    create_table(mysql_root_password)
    try:
        insert_to_database(mysql_root_password, title, username, encoded_password)
    except mc.IntegrityError:
        print(f"\n{'🛑'} Credentials For The Title Already Exist.")


# -- Fetches the password of the corresponding title and username ------------------
def fetch_password(mysql_root_password):
    print("\n---------------Fetching Password---------------")
    to_search_title = input("Enter the corresponding title/address: ")
    to_search_username = input("Enter the username: ")

    passwords_database = connect_to_database(mysql_root_password)
    passwords_cursor = passwords_database.cursor()
    search_query = "SELECT password FROM passwords WHERE username = %s AND title = %s"
    try:
        passwords_cursor.execute(search_query, (to_search_username, to_search_title,))
        password = passwords_cursor.fetchone()
        decoded_password = base64.b64decode(password[0])
        print(f"\n{'📘'} Your Password Is: {decoded_password.decode('utf-8')}")

    except TypeError:
        print(f"\n{'🛑'} Something Went Wrong...No Such Credentials Could Be Found.")


# -- Main flow ---------------------------------------------------------------------
print("\n---------------Password Manager Started---------------")
choice = ""
exit_main = 0
mysql_root_password = input("\nEnter your MYSQL root password: ")

if user_authentication():
    while not exit_main:
        print("\n1. New Credentials"
              "\n2. Fetch Credentials"
              "\n3. Exit")
        choice = input("\nChoose The Option (1, 2, 3): ")
        if choice == "1":
            new_password(mysql_root_password)
        elif choice == "2":
            fetch_password(mysql_root_password)
        elif choice == "3":
            print("See you!")
            exit_main = 1
        else:
            print("\nChoose The Option Correctly And Try Again...")
