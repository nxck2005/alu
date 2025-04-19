from flask import Flask, render_template

app = Flask(__name__)

@app.route('/alu')
def alu():
    return render_template("alu.html")