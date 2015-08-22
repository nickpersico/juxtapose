# hello.py

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from juxtapose import *
app = Flask(__name__)

Bootstrap(app)

@app.route("/")
def hello():
    return render_template(
        'index.html',
        juxtapose=jux_data,
        property_data=property_data,
        listing_data=listing_data
    )

if __name__ == "__main__":
    app.run(debug=True)
