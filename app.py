from flask import Flask, render_template, redirect, url_for
from alu import ALU, Memory
from helpers import Helper

alu = ALU(1)
mem = Memory(40)

app = Flask(__name__)

# Make helpers available in all templates
app.jinja_env.globals['helper'] = Helper

@app.route('/')
def alu_route():
    return render_template("content.html", aluObj=alu, memObj=mem)

@app.route('/execCycle', methods=['POST'])
def execCycle():
    alu.execute()
    return redirect(url_for('alu_route'))
    