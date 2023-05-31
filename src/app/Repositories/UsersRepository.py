from Class.UserMapper import userMapper
from Database.main import cursor, connection

class UsersRepository():
    def __init__(self):
        pass

    def findByUsername(self, username):
        cursor.execute(f'''
            SELECT * FROM users
            WHERE username = '{username}'
        ''')

        row = cursor.fetchone()

        return userMapper(row)

    def findByEmail(self, email):
        cursor.execute(f'''
            SELECT * FROM users
            WHERE email = '{email}'
        ''')

        row = cursor.fetchone()

        return userMapper(row)
    
    def findById(self, id):
        cursor.execute(f'''
            SELECT * FROM users
            WHERE id = '{id}'
        ''')

        row = cursor.fetchone()

        return userMapper(row)

    def create(self, username, email, password):
        cursor.execute(f'''
            INSERT INTO 
            users (username, email, password) 
            VALUES('{username}', '{email}', '{password}')
            RETURNING id
        ''')

        id = cursor.fetchone()[0]

        connection.commit()

        return id
    
    def update(self, id, newUsername, newEmail, newPassword):
        cursor.execute(f'''
            UPDATE users SET
            username = '{newUsername}',
            email = '{newEmail}',
            password = '{newPassword}'
            WHERE id = '{id}'
        ''')

        connection.commit()