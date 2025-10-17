from flask import Flask, request, render_template
from logger import log_creds

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def phishing_page():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        log_creds(email, password)
        return render_template("awareness.html")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
