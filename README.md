# Password Manager CLI

A **secure and easy-to-use Password Manager** built with **Python**.  
Store, view, edit, and delete your passwords safely using **Fernet encryption**.

---

## Features

- Add new passwords with encryption
- View saved passwords (decrypted on view)
- Edit existing passwords
- Delete passwords
- Secure local storage (`passwords.json`)
- Key management via `secret.key`

---

## Screenshots

Since this is a CLI application, here's a sample interaction:

![Password Maneger](https://github.com/Epanacode/Password_manager/blob/main/assets/2025-10-22%2002_03_34-main.py%20-%20Password_manager%20-%20Visual%20Studio%20Code.png?raw=true)


---

## Requirements

- Python 3.x
- [cryptography](https://pypi.org/project/cryptography/) library

Install dependencies:

    pip install cryptography

<hr/>

**How to Run**

1. Clone the repository:

          git clone https://github.com/your-username/PasswordManager.git
          cd PasswordManager
2. Run the program:

        python main.py

3. Use the menu to manage your passwords.

<hr/>

**Usage Instructions**

1️⃣ **Add new password:** Enter the site or application name and password.

2️⃣ **View saved passwords:** See all stored passwords (decrypted).

3️⃣ **Edit password:** Update a password for a specific site.

4️⃣ **Delete password:** Remove a saved password by site name.

5️⃣ **Exit:** Safely exit the program.

<hr/>

**Security Notes**

- All passwords are encrypted using **Fernet symmetric encryption.**

- Keep (`secret.key`)safe—without it, saved passwords cannot be decrypted.

- (`passwords.json`) stores all encrypted passwords locally.

<hr/>

**License**

This project is open-source under the MIT License.

<hr/>

💻Author:
 
 **Epanacode**
 
*Python Developer | Django & Telegram Bot Enthusiast*

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github)](https://github.com/Epanacode)

