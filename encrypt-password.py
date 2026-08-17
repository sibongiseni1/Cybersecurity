import bcrypt

name = input("Enter your name: ")
Surname = input("Enter your Last name: ")
Email= input("Enter your email: ")
password = input("Enter your password: ").encode()

salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password,salt)

user_db = {
    "Name": name,
    "Surname": Surname,
    "Email": Email,
    "Password": hashed_password
}

print("--------------USER INFORMATION----------------")
print("\n")
print(f"Your name: {user_db['Name']}")
print(f"Your Surname: {user_db['Surname']}")
print(f"Your Email: {user_db['Email']}")
print(f"Your name: {user_db['Password']}")