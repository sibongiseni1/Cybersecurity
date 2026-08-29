import hashlib

First_name = input("Enter your First name: ")
Surname = input("Enter your Last name: ")
Email= input("Enter your email: ")
password = input("Enter your password: ")

password_bytes = password.encode("utf-8")
sha_512 = hashlib.sha512(password_bytes).hexdigest()


user_info = f'''print("----------------------USER INFORMATION---------------------------------")
    
    "Your Full name: {First_name} {Surname}"
    "Your Email: {Email}"
    "Your password: {sha_512}"

'''
    

with open("user_info.log", "w") as f:
    f.write(user_info)

print(user_info)
