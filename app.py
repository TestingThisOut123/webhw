from flask import Flask, request, Response, render_template, url_for,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import Regexp,NumberRange
from flask_wtf.csrf import CSRFProtect
from helper import *
import re 
app = Flask(__name__)
app.config['SECRET_KEY']='baby'
alpbabet='abcdefghijklmnopqrtuvwxyz'
apikey=''

class mainForm(FlaskForm):
    inputstring=StringField("inputstring", validators= [Regexp(r'^[a-z]+$', message="must contain letters only")])
    stringsize=IntegerField("stringsize",validators=[NumberRange(min=3,max=10,message="must numbers between 3-10")])
    patternstring =StringField('patternstring')
    search=SubmitField("Get all strings")


csrf = CSRFProtect()

@app.route('/', methods=['GET','POST'])
def index():
    form=mainForm()
    letters=""
    wordsize=0
    pattern=""
    if form.validate_on_submit() and request.method=='POST':
        letters = form.inputstring.data
        wordsize = form.stringsize.data
        pattern = form.patternstring.data
        #suppose to have an else clause
    else:
        return render_template("main.html", form=form)
    if len(letters)==0 and len(pattern)==0:
        flash('You were successfully logged in') 
    elif len(letters)==0 and len(pattern)>0:
        if wordsize==0:
            #return all words that match the pattern
            # NEED TO CHECK THIS ONE
            return algo(alphabet,pattern,len(pattern))
        else:
            if len(pattern)==wordsize:
                #return all words that match the pattern
                return algo(alphabet,pattern,wordsize,"-reg")
            else:
                #print an error message to the user. 
                flash('You were successfully logged in')

    elif len(letters)>0 and len(pattern)==0:
        if wordsize==0:
            #return all words
            retur=algo(letters,"",10,"-all")
            return render_template('wordlist.html',wordlist=sorted(retur),name="CS4131")
        else:
            #return words with size
             retur=algo(letters,"",wordsize,"-reg")
             return render_template('wordlist.html',wordlist=sorted(retur),name="CS4131")

    elif len(letters)>0 and len(pattern)>0:
        if wordsize==len(pattern):
            #run it with pattern with size
            retur=algo(letters,pattern,wordsize,"-reg")
            return render_template('wordlist.html',wordlist=sorted(retur),name="CS4131")
        elif wordsize<3:
            return "run above"
        else:
            return "an error message"     
    return "hi"



@app.route('/proxy/<word>')
def proxy():
    print("i got here")
    apikey='9b621d3e-98b1-4b1b-b21a-4849d6d92e49'
    x = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={apikey}')
    return jsonify(x.json())



if __name__ == "__main__":
    app.run(debug=True)

