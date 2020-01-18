from werkzeug.security import generate_password_hash, check_password_hash
from marky import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    is_active = db.Column(db.Boolean())
    authenticated = db.Column(db.Boolean(), default=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = self.set_password(kwargs['password'])

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def change_password(self, new_password):
        self.password = self.set_password(new_password)

    def toggle_active(self):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True
        
        return self.is_active

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return self.activated

    def is_anonymous(self):
        """
            Returns False since there 
            are no anonymous users.
        """
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return "User(id='{self.id}', name='{self.username}', pw='{self.password}', email='{self.email}')".format(self=self)