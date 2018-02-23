from flask_restful import Api
from wtforms import StringField, ValidationError
from datetime import datetime
#from pytz import timezone
#import sqlite3
import requests
from flask import Flask, render_template, request, redirect, session, url_for, flash, send_file, send_from_directory
from flask_bootstrap import Bootstrap
from wtforms import TextAreaField, SubmitField, IntegerField, FloatField, StringField, SelectField, TextField
from wtforms.validators import DataRequired
from flask_wtf import Form, CSRFProtect
import os
from flask_restful import reqparse, Api, abort, Resource, fields, marshal





#----------------------------------------
# initialization
#----------------------------------------



app = Flask(__name__)
Bootstrap(app)
app.config.update(
    DEBUG = True,
)


api = Api(app)
csrf=CSRFProtect(app)

app.config['SECRET_KEY']="secret"

#----------------------------------------
# controllers
#----------------------------------------

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/icosa.ico')

#@app.errorhandler(404)
#def page_not_found(e):
 #   return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

#------------------
# Login
#------------------

@app.route('/showSignin')
def showSignin():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('signin.html')
    
@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')
@csrf.exempt
@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
       # cfile=open("configurations/credentials.txt", "r")
        #cData=cfile.read().split("\n")
        #cUser=cData[0].rstrip('\r')
        #cPassword=cData[1].rstrip('\r')
        #cfile.close()
        _username = request.form['inputUserName']
        _password = request.form['inputPassword']

        if _password == "lala" and _username == "lala":
            session['user'] = _username
            return redirect('/userHome')

        else:
            return render_template('error.html',error = 'Wrong UserName or Password.')

    except Exception as e:
        return render_template('error.html',error = str(e))



@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Unauthorized Access')



#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    print("Running on port 5000")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='localhost', port=port)
    #0.0.0.0
