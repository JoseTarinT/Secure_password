import secrets
import string

# We ask the users how many characters they want in the password
lenght = int(input("How many characters do you want in your password?: "))
characters = string.ascii_letters + string.digits + string.punctuation
# print(characters)

password = "".join(secrets.choice(characters) for x in range(lenght))

print("Your password is: ", password)