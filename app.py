from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)
app.config["SECRET_KEY"] = b'Ko5\xc8\x13w\x8b\x8c\xc8\xa9\xa5\xf0P\x92"\x12'

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/", methods=["GET"])
def start():
    """ Page where users can choose to register their account or log in to existing accounts """

    # Render start template
    return render_template("index.html")