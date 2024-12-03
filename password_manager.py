from cryptography.fernet import Fernet

def load_key():
   file = open("key.key", "rb").read()
   key = file.read()
   file.close()
   return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer= Fernet(key)

def write_key():
   key = Fernet.generate_key()
   with open("key.key", "wb") as key_file:
      key_file.write(key)


def view():
   with open('password.txt', 'r') as f:
      for line in f.readlines():
         data = line.rstrip()
         user, passw = data.split("|")
         print("User:", user, "Password:", str(fer.decryptcrypt(passw.encode())))

def add():
   name = input("Account name: ")
   pwd = input("Password: ")

   with open('password.txt', 'a') as f:
      f.write(name + "|" + str(fer.encrypt(pwd.encode()).decode()) + "\n")

while True:
 mode = input("Would you like to add a new password or view existing ones(view, add)? ").lower()

 if mode == "view":
    view()
 elif mode == "add":
    add()
 else:
    print("Invalid mode")
    continue