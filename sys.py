import sys
from codes import list

print("Welcome to VitaSync")
print("")
print("")
def program():
    while True:
        name = input("What's your name?")
        if name.isalpha():  # Check if the input contains only letters
            name = name.upper()
            break
        else:
            print("Invalid input. Please enter your name.")
    print(f"Hello {name}")

    while True:
        code = input("enter your cash code:")
        if code in list:
            print("all done")
            break
        elif code not in list:
            print("invalid code")
    while True:
        email = input("Enter your email address:")
        if "@" in email and email.count("@") == 1:
            local_part, domain = email.split("@")
            if local_part and domain:  # Check if there's something before and after the @ symbol
                if "." in domain:  # Check if there's a dot in the domain
                    break
                else:
                    print("Invalid email address. Please use a valid domain (e.g. example.com).")
            else:
                print("Invalid email address. Please enter something before and after the @ symbol.")
        else:
            print("Invalid email address. Please try again.")
while True:
    try:
        age = int(input("Enter your age:"))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if age in range(13, 19):
    print("HI")
    program()
elif age in range(19, 61):
    print("Hi")
    status = input("are you worker(Y/N)")
    status = status.lower
    if status == "y":
        print("HI")
        program()
elif age > 100:
    print("you must be dead now")
    sys.exit()
