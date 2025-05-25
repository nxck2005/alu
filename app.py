from flask import Flask, render_template, redirect, url_for, request, flash
from alu import ALU, Memory, maxValue, minValue
from helpers import Helper

alu = ALU(1)
mem = Memory(20)

app = Flask(__name__)
app.secret_key = 'IHateLilly69420'

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
    regno = request.form.get("regno")
    val = request.form.get("pokeval")
    print(f"RNO Recieved: {regno}")
    print(f"Val recieved: {val}")

    
    regno = int(regno)
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
    val = int(val, 16)
   
    # fallback error check
    if val > maxValue or val < minValue:
        flash("Value too big!", "success")
        
    mem.poke(rowno, val)
    return redirect(url_for('alu_route'))