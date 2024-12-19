from flask import Flask, render_template, redirect, url_for, request
from models import login_db, UserLogin
import authenticate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login_db.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        if authenticate.register_authenticate(userid, password):
            return redirect(url_for('login'))
        else:
            return render_template('signup.html', exists_error=True)
    return render_template('signup.html')

if __name__ == '__main__':
    with app.app_context():
        login_db.create_all()
    app.run(debug=True, port=8000)
