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

def verify_admin(username, password):
    mydb = connect_to_database()
    mycursor = mydb.cursor()

    sql = "SELECT * FROM admin WHERE adminName = %s"
    values = (username,)

    mycursor.execute(sql, values)
    admin = mycursor.fetchone()

    mycursor.close()
    mydb.close()

    if admin:
        stored_hash = admin[2]  # Assuming the hashed password is in the third column
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
            return True

    return False

if __name__ == "__main__":
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if verify_admin(username, password):
        print("Admin login successful. Proceed to query.py.")
    else:
        print("Invalid admin credentials. Exiting.")
