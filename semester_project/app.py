# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Route for the index page
@app.route('/')
def index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
