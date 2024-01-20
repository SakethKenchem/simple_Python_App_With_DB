import mysql.connector
import bcrypt


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="S00per-d00per",
    database="mydatabase"
)

mycursor = mydb.cursor()

# Function to hash the password using bcrypt
def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

# Get user input
name = input("Enter your name: ")
password = input("Enter your password: ")

# Hash the password
hashed_password = hash_password(password)

# Store user information in the database
sql = "INSERT INTO users (name, password) VALUES (%s, %s)"
values = (name, hashed_password)

mycursor.execute(sql, values)

mydb.commit()

print("User successfully registered!")

# Close the database connection
mycursor.close()
mydb.close()
