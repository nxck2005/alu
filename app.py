from flask import Flask, render_template, redirect, url_for, request, flash
from alu import ALU
from memory import Memory
from helpers import Helper
from microcode import instructionSet
from constants import maxValue, minValue, __version__, __author__
import json
import logging
import loggingConfig as lc
import os
from dotenv import load_dotenv

load_dotenv()

lc.loggingConfigure()
al = logging.getLogger(__name__)

alu = ALU()
mem = Memory(40)

# dump instruction set as a variable w json
insJson = json.dumps(instructionSet, indent=4)
al.info("Instruction set: %s", insJson)

# dump instruction set to file
try:
    with open("instructionSet.json", "x") as f: 
        f.write(insJson)
        al.info("Instruction set dumped, file not present")
except FileExistsError:
    with open("instructionSet.json", "w") as f:
        f.write(insJson)
        al.info("Instruction set dumped; File existed, overwritten")
        
    
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-key')
al.info("Flask web app initialised")

# make helpers class available in all templates
# call using helper.x
app.jinja_env.globals['helper'] = Helper
al.info("Helpers initialised for use")

@app.route('/')
def alu_route():
    al.info("Index route called")
    return render_template("content.html", aluObj=alu, memObj=mem, version=__version__, author=__author__)

@app.route("/resetALU", methods=['POST'])
def resetALU():
    al.info("Reset ALU route called")
    alu.reset()
    al.info("ALU resetted!")
    return redirect(url_for('alu_route'))

@app.route("/resetMem", methods=['POST'])
def resetMem():
    al.info("Reset mem route called")
    mem.reset()
    al.info("Memory resetted!")
    return redirect(url_for('alu_route'))

@app.route('/execCycle', methods=['POST'])
def execCycle():
    al.info("Execute route called")
    alu.execute(mem, mem.MEMORY[alu.pc])
    return redirect(url_for('alu_route'))

@app.route('/pokeALU', methods=['POST'])
def pokeALU():
    al.info("Poke ALU route called")
    try:
        regno = request.form.get("regno")
        val = request.form.get("pokeval")
        
        print(f"RNO Recieved: {regno}")
        print(f"Val recieved: {val}")
        
        regno = int(regno)
        
        # cast val into an int w base 16; hence hex value
        val = int(val, 16)
    except:
        al.error("An error occured while fetching or decoding value. Empty field?")
        return redirect(url_for('alu_route'))

    # fallback error check
    if val > maxValue or val < minValue:
        flash("Value too big!", "success")
    
    alu.poke(val, regno)
    return redirect(url_for('alu_route'))

@app.route('/pokeMem', methods=['POST'])
def pokeMem():
    al.info("Poke memory route called")
    try:
        rowno = request.form.get("rowno")
        val = request.form.get("rowval")
        
        print(f"Row number recieved: {rowno}")
        print(f"Val recieved: {val}")
        
        rowno = int(rowno)
        
        # cast val into an int w base 16; hence hex value
        val = int(val, 16)
    except:
        al.error("An error occured while fetching or decoding value. Empty field?")
        return redirect(url_for('alu_route'))

    # fallback error check
    if val > maxValue or val < minValue:
        flash("Value too big!", "success")
        
    mem.poke(rowno, val)
    return redirect(url_for('alu_route'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 6969)), debug=False)