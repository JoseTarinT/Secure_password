import secrets
import string

# We ask the users how many characters they want in the password
lenght = int(input("How many characters do you want in your password?: "))
combinations =  ["A: Just letters", "B: Just numbers/digits", "C: Numbers and letters", "D: Letters and special characters", "E: Numbers and special characters", "F: Letters, numbers and special characters"]
print("What type of password would you prefer?")

for choices in combinations:
    print(choices)
    
passwordtype = str.lower(input())

characters = string.ascii_letters + string.digits + string.punctuation
a = string.ascii_letters
b = string.digits
c = a + b
d = a

password = "".join(secrets.choice(passwordtype) for x in range(lenght))

if passwordtype == a:
    print("Your password is: ", password)
characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(secrets.choice(characters) for x in range(lenght))

print("Your password is: ", password)
