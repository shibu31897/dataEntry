from flask import Flask, render_template, request
from login import Login

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        email = request.form.get("user_email")
        password = request.form.get("password")
        l = Login(email, password).login()
        if l == True:
            return render_template("dataEntry.html")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
