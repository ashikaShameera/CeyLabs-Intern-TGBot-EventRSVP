import sqlite3
import datetime

class DatabaseHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables_if_not_exist()
        print("Database Connected")

    def create_tables_if_not_exist(self):
        self.cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='user' ''')
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute('''
            CREATE TABLE user (
                user_id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT UNIQUE
            )
            ''')
        self.cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='ticket' ''')
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute('''
            CREATE TABLE ticket (
                ticket_id INTEGER PRIMARY KEY,
                event_name TEXT,
                issue_date TEXT,
                event_date TEXT,
                user_id INTEGER,
                created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(user_id)
            )
            ''')

        self.conn.commit()

    def insert_user(self, name, email):
        self.cursor.execute('''
        INSERT INTO user (name, email)
        VALUES (?, ?)
        ''', (name, email))
        self.conn.commit()

    def insert_ticket(self, event_name, event_date, user_id):
        issue_date = datetime.datetime.now().strftime('%Y-%m-%d')  # Get current date in 'YYYY-MM-DD' format
        created_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current date and time in 'YYYY-MM-DD HH:MM:SS' format
        self.cursor.execute('''
        INSERT INTO ticket (event_name, issue_date, event_date, user_id, created_time)
        VALUES (?, ?, ?, ?, ?)
        ''', (event_name, issue_date, event_date, user_id, created_time))
        self.conn.commit()


    def get_user_id(self, email):
        self.cursor.execute('''
        SELECT user_id FROM user WHERE email = ?
        ''', (email,))
        result = self.cursor.fetchone()
        if result:
            return result[0]  # Return user_id if email exists
        else:
            return None  # Return None if email doesn't exist
        
    def get_tickets_by_email(self, email, limit):
        self.cursor.execute('''
        SELECT * FROM ticket
        WHERE user_id = (SELECT user_id FROM user WHERE email = ?)
        ORDER BY created_time DESC
        LIMIT ?
        ''', (email, limit))
        tickets = self.cursor.fetchall()
        return tickets
