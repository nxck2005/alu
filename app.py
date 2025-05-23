from flask import Flask, render_template
from alu import ALU, Memory

alu = ALU(1)
mem = Memory(40)

app = Flask(__name__)

@app.route('/')
def alu_route():
    print(alu.REGISTERS)
    return render_template("content.html", aluObj=alu, memObj=mem)