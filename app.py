from flask import Flask, render_template

app = Flask(__name__)

@app.route('/alu')
def alu():
    return "there'll be something here someday ;)"