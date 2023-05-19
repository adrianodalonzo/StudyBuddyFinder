from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, password):
        if not isinstance(username, str):
            raise TypeError('Username must be a string')
        if not isinstance(password, str):
            raise TypeError('Password must be a string')
        
        self.username = username
        self.password = password

        self.id = None