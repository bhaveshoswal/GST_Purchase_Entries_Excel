# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import csv
import pandas as pd

# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
# @app.route('/')
# def home():
#     return "Hello, World!"  # return a string


@app.route('/welcome')
def welcome():
    with open('config/companies.csv') as f:
        lists = dict(filter(None, csv.reader(f)))

    return render_template('welcome.html', lists=lists)  # render a template


@app.route('/to_excel', methods=["POST"])
def export_excel():
    table_data = request.form['table_data']
    df = pd.read_html(table_data)[0]
    df.to_excel("purchase_entries.xlsx", index=False)

    return "Success!!!"


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
