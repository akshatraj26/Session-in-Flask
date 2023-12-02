from flask import Flask, render_template, url_for, session, request, make_response

app = Flask(__name__)
# app.config['SECRET_KEY'] = "sessionconcept"
app.secret_key = 'login'

@app.route('/')
def index():
    return render_template('login.html')
    
@app.route("/login", methods=['POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        if (username == 'clarkfirth') and (password == "clarkfirth123"):
            session['name'] = username
            return render_template('success.html', name = username)
        else:
            msg = "Invalid Username or password"
            return render_template('login.html', msg = msg)
        


        
@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template("login.html")


@app.route('/profile')
def profile():
    if 'name' in session:
        name = session['name']
        return render_template('profile.html', name = name) 
    else:
        return render_template('login.html', msg = "Login first")


if __name__ == "__main__":
    app.run(debug=True)