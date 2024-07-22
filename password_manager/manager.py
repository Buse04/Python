import sys

manager = input("\nWhat is your pasword? : ")

def add():
    name = input("\nAccount name: ")
    global manager
    manager = input("\nNew password: ")
    with open ('passwords.txt' , 'a') as f:
        f.write(name + "|" + manager + "\n")

def view():
    with open ('passwords.txt' , 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "Password: ", passw)

while True:

    mode = input("\nWould you like to add a new password or view existing ones (view, add)? : (press q to quit)").lower()

    if mode == str("q"):
        sys.exit()
    if mode == str("view"):
        view()
    elif mode == str("add"):
        add()
    else:
        print("\nInvalid mode")

