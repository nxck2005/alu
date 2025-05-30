from flask import Flask, render_template, redirect, url_for, request, flash
from alu import ALU
from memory import Memory
from helpers import Helper
from microcode import instructionSet
from constants import maxValue, minValue, __version__, __author__
import json
import logging
import loggingConfig as lc

lc.loggingConfigure()
applogger = logging.getLogger(__name__)

alu = ALU()
mem = Memory(40)

# dump instruction set as a variable w json
insJson = json.dumps(instructionSet, indent=4)
applogger.info("Instruction set dumped: %s", insJson)
print("Instruction set:", insJson)

# write that json to file
try:
    with open("instructionSet.json", "w") as f:
        f.write(insJson)
except:
    f = open("instructionSet.json", "x")
    f.write(insJson)
    f.close()

app = Flask(__name__)
app.secret_key = 'IHateLilly69420'

# make helpers class available in all templates
# call using helper.x
app.jinja_env.globals['helper'] = Helper

@app.route('/')
def alu_route():
    return render_template("content.html", aluObj=alu, memObj=mem, version=__version__, author=__author__)

@app.route("/resetALU", methods=['POST'])
def resetALU():
    alu.reset()
    return redirect(url_for('alu_route'))

@app.route("/resetMem", methods=['POST'])
def resetMem():
    mem.reset()
    return redirect(url_for('alu_route'))

@app.route('/execCycle', methods=['POST'])
def execCycle():
    alu.execute(mem)
    return redirect(url_for('alu_route'))

@app.route('/pokeALU', methods=['POST'])
def pokeALU():
    regno = request.form.get("regno")
    val = request.form.get("pokeval")
    print(f"RNO Recieved: {regno}")
    print(f"Val recieved: {val}")
    
    regno = int(regno)
    
    # cast val into an int w base 16; hence hex value
    val = int(val, 16)
    
    # fallback error check
    if val > maxValue or val < minValue:
        flash("Value too big!", "success")
    
    alu.poke(val, regno)
    return redirect(url_for('alu_route'))

@app.route('/pokeMem', methods=['POST'])
def pokeMem():
    rowno = request.form.get("rowno")
    val = request.form.get("rowval")
    
    print(f"Row number recieved: {rowno}")
    print(f"Val recieved: {val}")
    
    rowno = int(rowno)
    
    # cast val into an int w base 16; hence hex value
    val = int(val, 16)
   
    # fallback error check
    if val > maxValue or val < minValue:
        flash("Value too big!", "success")
        
    mem.poke(rowno, val)
    return redirect(url_for('alu_route'))

@app.route('/exec', methods=['POST'])
def exec():
    pass