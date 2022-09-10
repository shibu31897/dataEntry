from flask import Flask, render_template, request,session,redirect
from login import Login
import pyrebase
from cred import firebaseConfig,secretKey
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__)
app.secret_key = secretKey

@app.route("/", methods=['POST', 'GET'])
def index():
    if 'user' in session:
        return render_template("dataEntry.html")
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def login():
    if 'user' in session:
        return render_template("dataEntry.html")
    if request.method == "POST":
        email = request.form.get("user_email")
        password = request.form.get("password")
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            session['user'] = email
        except:
            return "Failed to Login"
    return render_template("index.html")



@app.route("/logout")
def logout():
    session.pop('user')
    return redirect("/")


@app.route("/dataEntry")
def dataEntry():
    return render_template("dataEntry.html")


if __name__ == '__main__':
    app.run(debug=True)
