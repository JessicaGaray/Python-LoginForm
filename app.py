import time
from flask import Flask, render_template, request, session, redirect, url_for, escape, make_response

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/login')
def login_form():
   return render_template('login_form.html')

@app.route('/login', methods=['POST'])
def login_user():
   session['email'] = request.form['email']
   session['password'] = request.form['password']
   if session['email'] == 'test@flask.app' and session['password'] == 'password123':
      return redirect(url_for('session_user', email = session['email'], password = session['password']))
   else:
      return render_template('invalid_login.html')

@app.route('/my-profile')
def session_user():
   
   email = session['email']
   password = session['password']
   if 'email' not in session and 'password' not in session:
      resp = make_response (render_template('login_wosession.html', email=escape(session['email']), password=escape(session['password']),))
   if 'email' in session and 'password' in session:
      resp = make_response(render_template('valid_login_withsession.html', email=escape(session['email']), password=escape(session['password'])))
   resp.set_cookie('email', email)
   resp.set_cookie('password', password)
   return resp
   
   return render_template('invalid_login.html')
   
@app.route('/logout')
def logout():
   # remove the username from the session if it's there
   if session.get('email'):
      session.pop('email', None)
   if session.get('password'):
      session.pop('password', None)
   return render_template('logout.html')

app.run(debug=True)