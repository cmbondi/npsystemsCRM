from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def Main():
    return render_template('index.html')

@app.route('/detail')
def Detail():
    return render_template('detail.html')

@app.route('/add')
def Add():
    return render_template('add.html')

@app.route('/edit')
def Edit():
    return render_template('edit.html')