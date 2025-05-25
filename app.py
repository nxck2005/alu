from flask import Flask, render_template, redirect, url_for, request
from alu import ALU, Memory
from helpers import Helper

alu = ALU(1)
mem = Memory(20)

app = Flask(__name__)

# make helpers class available in all templates
# call using helper.x
app.jinja_env.globals['helper'] = Helper

@app.route('/')
def alu_route():
    return render_template("content.html", aluObj=alu, memObj=mem)

@app.route('/execCycle', methods=['POST'])
def execCycle():
    alu.execute(mem)
    return redirect(url_for('alu_route'))

@app.route('/pokeALU', methods=['POST'])
def pokeALU():
    regno = request.form.get()
    pass
    