from cryptography.fernet import Fernet 

#Uncomment the following code to generate key the comment again after the key has been generated

# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_value:
#         key_value.write(key)

# write_key()

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_store_password(masterPwd):
    key = load_key()
    fer = Fernet(key)
    encryptedMasterPwd = fer.encrypt(masterPwd.encode())
    with open ('master_pwd.txt', 'wb') as master_pwd_file:
        master_pwd_file.write(encryptedMasterPwd)

def load_decrypt_master_pwd():
    key = load_key()
    with open ('master_pwd.txt', 'rb') as master_pwd_file:
        encryptedMasterPwd = master_pwd_file.read()
        fer = Fernet(key)
        decryptedMasterPwd = fer.decrypt(encryptedMasterPwd).decode()
        return decryptedMasterPwd


def add():
    key = load_key()
    fer = Fernet(key)
    accName = input("Input account name:")
    pwd = input("Input " + accName + " password: ")
    with open('password.txt', 'a') as f:
        f.write(accName + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    key = load_key()
    fer = Fernet(key)
    with open('password.txt', 'r') as f:
            lines = f.readlines()
            if not lines:
                print("No passwords stored.")
            else:
                for line in lines:
                    data = line.rstrip()
                    name, password = data.split("|")
                    print("Account Name:" + name + ", Password:", fer.decrypt(password.encode()).decode())

master_pwd_exists = False 

while True:
    key = load_key()
    try:
        with open("master_pwd.txt", "r") as f:
            lines = f.readlines()
            if lines:
                master_pwd_exists = True
    except FileNotFoundError:
        master_pwd_exists = False

    if not master_pwd_exists:
        masterPwd = input("Create your master password: ")
        encrypt_store_password(masterPwd)
        print("Master password created and stored securely.")
    else:
        user = input("Do you want to add new password or view existing passwords?(Choose 'add' or 'view' or 'Q' to quit): ").lower()
        if user == 'q':
            print("Quitting....")
            break
        elif user == 'add' or user == 'view':
            masterPwd = input("Type your master password: ")
            decrypted_master_pwd = load_decrypt_master_pwd().encode()
            if masterPwd.encode() == decrypted_master_pwd:
                if user == 'add':
                    add()
                elif user == 'view':
                    view()
            else:
                print("Invalid mater password. Quitting...")
                break
        else:
            print("Invalid option! Quitting...")
            break
