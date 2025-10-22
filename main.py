from functions import *


while True:
    print("\n--- Password Manager ---")
    print("1. Add new password")
    print("2. View saved passwords")
    print("3. Delete a password")
    print("4. Edit password")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_password()
    elif choice == "2":
        if not passwords:
            print("No passwords saved yet.")
        else:
            for site_name, encrypted in passwords.items():
                real = decrypt_password(encrypted)
                print(f"{site_name} : {real}")
    elif choice == "3":
        for site_name, encrypted in passwords.items():
            real = decrypt_password(encrypted)
            print(f"{site_name} : {real}")
        delete_password()
    elif choice == "4":
        edit_password()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
