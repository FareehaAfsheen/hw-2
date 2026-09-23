# 🏦 Bank Management System — Python OOP

A simple **Bank Management System** built with Python to practice **Object-Oriented Programming (OOP)** concepts.

The program allows users to create bank accounts, view account information, check balances, and delete accounts through a menu-driven interface.

## 📌 Features

* Create a new bank account
* Store account holder's name and balance
* Show all accounts
* Check account balance
* Deposit money
* Withdraw money
* Transfer money *(planned / to be implemented)*
* Delete an account
* Exit the system

## 🧠 OOP Concepts Used

### 1. Classes and Objects

The `BankAccount` class represents a bank account.

```python
class BankAccount:
```

Each account is created as an object:

```python
new_acc = BankAccount(name, balance)
```

### 2. Encapsulation

The account balance is stored as a **private attribute**:

```python
self.__balance = balance
```

Because `__balance` is private, it is accessed through methods such as:

```python
get_balance()
deposit()
withdraw()
```

This demonstrates the concept of **encapsulation**.

### 3. Methods

The `BankAccount` class contains several methods:

| Method          | Purpose                                      |
| --------------- | -------------------------------------------- |
| `show()`        | Displays account information                 |
| `deposit()`     | Adds money to the account                    |
| `withdraw()`    | Withdraws money if sufficient balance exists |
| `get_balance()` | Returns the current balance                  |

### 4. Functions

The program also uses a separate function:

```python
find_account(accounts, name)
```

This searches through the list of accounts and returns the account matching the given name.

## 📂 Program Structure

```text
Bank Management System
│
├── BankAccount
│   ├── name
│   ├── __balance
│   ├── show()
│   ├── deposit()
│   ├── withdraw()
│   └── get_balance()
│
├── find_account()
│
└── Main Menu
    ├── Add Account
    ├── Show All Accounts
    ├── Check Balance
    ├── Deposit
    ├── Withdraw
    ├── Transfer Money
    ├── Delete Account
    └── Exit
```

## ▶️ How to Run

Make sure Python is installed.

Run the program using:

```bash
python main.py
```

The program will display a menu:

```text
--Bank Management System--
1. Add Account
2. Show All Accounts
3. Check Balance
4. Deposit
5. Withdraw
6. Transfer Money
7. Delete Account
8. Exit
```

Enter the number corresponding to the operation you want to perform.

## ⚠️ Current Limitations

The **Deposit**, **Withdraw**, and **Transfer Money** options are included in the menu, but the current version only implements the logic for:

* Add Account
* Show All Accounts
* Check Balance
* Delete Account
* Exit

The deposit, withdrawal, and money-transfer operations can be connected to the menu in a future version.

## 🎯 Purpose

This project was created as a Python OOP practice project to understand:

* Classes and objects
* Constructors
* Encapsulation
* Private attributes
* Instance methods
* Lists of objects
* Searching through objects
* Menu-driven programs
* Basic banking operations