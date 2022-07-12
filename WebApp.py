from flask import Flask
from flask import Flask, render_template, url_for, flash, redirect
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '3b99d30fc6b3edf785b2ba93ae35e0c6'

@app.route("/")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    print('hello world')