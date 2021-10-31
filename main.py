from flask import Flask, render_template, request, redirect, url_for
from database import *

app = Flask(  # Create a flask app
    __name__, )

app.config['SECRET_KEY'] = 'changeme'

# TODO: Add all of the routes you want below this line!


@app.route("/")
def index():
    print(query_all())
    return render_template("index.html")


@app.route('/home')
def home():
  return render_template("home.html")
@app.route('/song1')
def song1():
  return render_template("song1.html")
@app.route('/song2')
def song2():
  return render_template("song2.html")
@app.route('/song3')
def song3():
  return render_template("song3.html")

@app.route('/Lyrics1')
def Lyrics1():
  return render_template("Lyrics1.html")
@app.route('/Lyrics2')
def Lyrics2():
  return render_template("Lyrics2.html")
@app.route('/Lyrics3')
def Lyrics3():
  return render_template("Lyrics3.html")


@app.route('/sheets1')
def sheets1():
  return render_template("sheets1.html")
@app.route('/sheets2')
def sheets2():
  return render_template("sheets2.html")
@app.route('/sheets3')
def sheets3():
  return render_template("sheets3.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
      uname = request.form['username']
      pword = request.form['password']
      user = query_by_name(uname)
      if user != None : #if user is found
          if pword == user.password:
            return redirect(url_for('home'))
          else:
            return render_template('login.html')
      else:
        return render_template("login.html")
    else:
      return render_template("login.html")
      

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        add_user(request.form['fullname'],request.form['gmail'],
        request.form['password'])
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
