import hashlib
password = input("Enter the password:")
upper = 0
lower = 0
special = 0
digit = 0
for ch in password:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    else:
        special += 1

print("\n Password Analysis:")
print("Length of the password:",len(password))
print("Upper characters:",upper)
print("Lower characters:",lower)
print("Digits present:",digit)
print("Special Characters present:",special)
if len(password)>=8 and upper and lower and special and digit:
    print("Password Strength: Excellent")
elif len(password)>=6 and (upper + lower + digit + special >= 3):
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")

print("\n Suggestions:")
if upper==0:
    print("Make sure atleast one upper character is present")
if lower==0:
    print("Make sure atleast lower character is present")
if special==0:
    print("Make sure atleast one special character is present")
if digit==0:
    print("Make sure atleast one digit is present")
else:
    print("No improvements are necessary")

while True:
    confpd = input("Confirm Password:")
    if password == confpd:
        print("Password confirmed successfully!")
        break
    else:
        print("Password Mismatch")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("\nHashed Password:")
print(hashed_password)

login_pwd = input("\nEnter password again for login verification: ")
login_hash = hashlib.sha256(login_pwd.encode()).hexdigest()

if login_hash == hashed_password:
    print("Login successful!")
else:
    print("Incorrect password!")

