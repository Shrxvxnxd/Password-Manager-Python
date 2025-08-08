Password-Manager-Python
A Password Manager in Python can generate strong, random passwords and save them in a CSV file for easy access. Using modules like `random` and `csv`, it can create secure passwords based on user preferences and store them with account details. This offers a quick, simple, and organized way to manage and retrieve credentials.

Features
- Generate strong passwords with lowercase, uppercase, digits, and special characters
- Save account name, username, password, and timestamp to a CSV file
- Simple and easy-to-use
- Works with Python's built-in modules only

Project Structure
```

Password-Manager-Python/
├── main.py   # Main script
├── generated_passwords.csv # Stored credentials
├── utils.py         
└── README.md             # Documentation


Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Password-Manager-Python.git
   cd Password-Manager-Python
```

2. Run the script:

   ```bash
   python main.py
   ```

Usage

1. Enter account details.
2. Choose password length and character types.
3. Generated password will be displayed and saved to `generated_passwords.csv`.

Example console output:

```
{Number of users} passwords saved to 'generated_passwords.csv' successfully!
```

Example CSV content:

```
S.No,Timestamp,Username,Password,Length
1,2025-08-08 09:43:46,Unknown,dbKk0!91,8
```

Modules Used

* `random`
* `csv`
* `datetime`

Security Note

This project stores passwords in plain text.
For real use, consider encrypting passwords.

