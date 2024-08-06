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
    try:
        age = int(input("Enter your age:"))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if age in range(13, 19):
    print("HI")
    program()
else:
    print("you are not in the age range (we target the teens)")