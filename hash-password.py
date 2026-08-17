import hashlib

First_name = input("Enter your First name: ")
Surname = input("Enter your Last name: ")
Email= input("Enter your email: ")
password = input("Enter your password: ")

password_bytes = password.encode("utf-8")
sha_512 = hashlib.sha512(password_bytes).hexdigest()

print("----------------------USER INFORMATION---------------------------------")
print("\n")
print(f"Your Full name: {First_name} {Surname}")
print(f"Your Email: {Email}")
print(f"Your password: {sha_512}")
