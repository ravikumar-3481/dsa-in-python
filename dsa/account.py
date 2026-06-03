import sqlite3 as sq3
import time

class Account:
    def __init__(self):
        pass

    def save_to_db(self, account_record ):
        conn = sq3.connect('account.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS accounts
                          (accountnumber INTEGER PRIMARY KEY,
                          accoountname TEXT NOT NULL,
                          accounttype TEXT NOT NULL,
                          balance REAL)''')
        for accountnumber, accoountname, accounttype, balance in account_record:
            cursor.execute('INSERT INTO accounts VALUES (?, ?, ?, ?)',
                           (accountnumber, accoountname, accounttype, balance))
        conn.commit()
        conn.close()

account = Account()
account_record = [(1001, 'John Doe', 'Savings', 5000.0),
                  (1002, 'Jane Smith', 'Checking', 3000.0),
                  (1003, 'Alice Johnson', 'Savings', 7000.0),
                  (1004, 'Bob Brown', 'Checking', 2000.0),
                  (1005, 'Charlie Davis', 'Savings', 6000.0),
                  (1006, 'Diana Evans', 'Checking', 4000.0),
                  (1007, 'Ethan Wilson', 'Savings', 8000.0),
                  (1008, 'Fiona Clark', 'Checking', 3500.0),
                  (1009, 'George Miller', 'Savings', 9000.0),
                  (1010, 'Hannah Lee', 'Checking', 2500.0),
                  (1011, 'Ian Turner', 'Savings', 7500.0),
                  (1012, 'Jessica Adams', 'Checking', 4500.0),
                  (1013, 'Kevin Scott', 'Savings', 8500.0),
                  (1014, 'Laura Green', 'Checking', 3000.0),
                  (1015, 'Michael Harris', 'Savings', 9500.0),
                  (1016, 'Nina Baker', 'Checking', 4000.0),
                  (1017, 'Oliver King', 'Savings', 10000.0),
                  (1018, 'Paula Wright', 'Checking', 5000.0),
                  (1019, 'Quentin Young', 'Savings', 11000.0),
                  (1020, 'Rachel Hill', 'Checking', 3500.0),
                  (1021, 'Samuel Turner', 'Savings', 8000.0),
                  (1022, 'Tina Scott', 'Checking', 4500.0),
                  (1023, 'Uma Adams', 'Savings', 9000.0),
                  (1024, 'Victor Green', 'Checking', 3000.0),
                  (1025, 'Wendy Harris', 'Savings', 9500.0),
                  (1026, 'Xavier Baker', 'Checking', 4000.0),
                  (1027, 'Yvonne King', 'Savings', 10000.0),
                  (1028, 'Zachary Wright', 'Checking', 5000.0),
                  (1029, 'Aaron Young', 'Savings', 11000.0),
                  (1030, 'Beth Hill', 'Checking', 3500.0)]

account.save_to_db(account_record)
time.sleep(1)  # Simulate some processing time
print("Account records have been saved to the database.")
