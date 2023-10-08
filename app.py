from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import datetime

app = Flask(__name__)
app.secret_key = "secret_key"  # Change this to a random secret key

app = Flask(__name__)
app.secret_key = "2378F98"  # Change this to a random secret key

# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['my_database']
users_collection = db['usersCollection']

@app.route('/')
def root():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # You should add code here to store users (use a database in a real app)
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # You should add code here to check users credentials (use a database in a real app)
        user_data = {
            'username': username,
            'login_time': datetime.datetime.now()  # Import datetime module
        }
        users_collection.insert_one(user_data)

        session['username'] = username
        return redirect(url_for('welcome'))
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        return render_template('welcome.html', username=username)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

