from ossaudiodev import SNDCTL_DSP_SPEED
from flask import Flask, jsonify, redirect, render_template, session, url_for, request
from flask_session import Session

from Controllers.AppController import AppController

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

ac = AppController()


@app.route("/login", methods=["POST", "GET"])
def Login():
  error = None
  if request.method == 'POST':
    print(request.form['email'])
    print(request.form['password'])
    print(ac.Login(request.form['email'], request.form['password']))
    
    if not ac.Login(request.form['email'], request.form['password']):
      error = 'Invalid Email or Password. Please try again.'
    else:
      session["email"] = request.form['email']
      print("success")
      return redirect('/home')
      
  return render_template('login.html', error = error)

@app.route("/home", methods=['GET'])
def home():
  return render_template('home.html', user = ac.GetUser(session['email']))

@app.route('/register', methods=['POST', 'GET'])
def register():
  
  error = None
  if request.method == 'POST':
    result = ac.Register(request.form['email'], request.form['password'], request.form['username'])
    if not result == 'None':
      error = result
    else:
      return redirect('/login')
    
  return render_template('register.html', error = error)
        
    

if __name__ == "__main__":
  app.run(debug=True)