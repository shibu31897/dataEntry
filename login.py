import pyrebase
import pyrebase as firebase
from cred import firebaseConfig


class Login:
    def __init__(self, email, password):
        self.firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth = self.firebase.auth()
        self.email = email
        self.password = password

    def signUp(self, email, password):
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            print("Successfully Signed Up")
            return True
        except:
            print("Something went wrong")
            return False

    def login(self):
        try:
            login = self.auth.sign_in_with_email_and_password(self.email, self.password)
            print("Successfully Signed In")
            return login
        except:
            print("Something went wrong")
            return False
