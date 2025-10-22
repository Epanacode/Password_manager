from cryptography.fernet import Fernet, InvalidToken
import os
import json

def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return key

key = load_key()
fernet = Fernet(key)

# فایل JSON رو لود کنیم یا بسازیم — باید **قبل از نمایش منو** باشه
if os.path.exists("passwords.json"):
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
else:
    passwords = {}
# تابع ذخیره سازی پسور
def save_password(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=2)
# تابع اضافه کردن پسورد
def add_password():
    site_name = input("Enter name site or application : ")
    if site_name in passwords:
        ans = input(f"{site_name} exists. Overwrite? (y/n): ")
        if ans.lower() != "y":
            print("Cancelled.")
            return
    password = input("Enter your password : ")
    encrypted = fernet.encrypt(password.encode())
    passwords[site_name] = encrypted.decode()
    save_password(passwords)
    print(f"{site_name} saved successfully!")

# تابع بازگشایی پسورد
def decrypt_password(encrypted):
    try:
        return fernet.decrypt(encrypted.encode()).decode()
    except InvalidToken:
        return "<Invalid or corrupted password>"
# تابع حذف پسورد
def delete_password():
    site = input("Enter site name to delete : ")
    if site in passwords:
        del passwords[site]
        save_password(passwords)
        print(f"Password for {site} updated successfully!!")
    else:
        print(f"{site} not found")
# تابع ویرایش رمز عبور
def edit_password():
    site = input("Enter site name to edit : ")
    if site in passwords:
        print(f"Current password for {site} is: {decrypt_password(passwords[site])}")
        new_password = input("Enter new password : ")
        encrypted = fernet.encrypt(new_password.encode())
        passwords[site] = encrypted.decode()
        save_password(passwords)
        print(f"password {site} updated successfully!!")
    else:
        print(f"{site} not found!!")
