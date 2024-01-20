import mysql.connector
import bcrypt

def connect_to_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S00per-d00per",
        database="mydatabase"
    )
    return mydb

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def admin_signup():
    admin_name = input("Enter your admin username: ")
    admin_password = input("Enter your admin password: ")

    mydb = connect_to_database()
    mycursor = mydb.cursor()

    hashed_password = hash_password(admin_password)

    sql = "INSERT INTO admin (adminName, adminPassword) VALUES (%s, %s)"
    values = (admin_name, hashed_password)

    try:
        mycursor.execute(sql, values)
        mydb.commit()
        print("Admin registration successful.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Admin registration failed.")

    mycursor.close()
    mydb.close()

if __name__ == "__main__":
    admin_signup()
