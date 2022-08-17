"""Server for BC Pham's personal website"""

from flask import Flask, render_template, redirect, flash, session
import jinja2

app = Flask(__name__)

app.secret_key = 'this-should-be-something-unguessable'

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)