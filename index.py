masterPwd = input("Hello, type your master password: ")
def add():
    accName = input("Input account name:")
    pwd = input("Input " + accName + " password: ")
    with open('password.txt', 'a') as f:
        f.write(accName + "|" + pwd + '\n')
    pass

def view():
    with open('password.txt', 'r') as f:
       for line in f.readlines():
           data = line.rstrip()
           name, pwd = data.split("|")
           print("Account Name: " + name + ", Password: " + pwd )
    pass

while True:
    user= input("Do you want to add new password or view existing passwords?(Choose 'add' or 'view' or 'Q' to quit): ").lower()
    if user == 'q':
        print("quiting....")
        break
    elif user == 'add':
        add()
        pass
    elif user == 'view':
        view()
        pass
    else:
        print("Invalid option! Quiting...")
        quit()