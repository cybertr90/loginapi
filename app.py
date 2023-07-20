from flask import Flask,request,render_template,flash,redirect,jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from flask_bcrypt import Bcrypt
from sqlalchemy import text
from dataclasses import dataclass
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.engine.cursor import CursorResult
import jwt
from functools import wraps
from datetime import datetime,timedelta

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config['SECRET_KEY'] = "thisisasecretkey"

db.init_app(app)

with app.app_context():
    db.create_all()

#Create JWT for User
def token(username):
    payload = {"sub":username,"exp":datetime.utcnow()}
    encoded_jwt = jwt.encode(payload,app.config['SECRET_KEY'],algorithm='HS256')
    return {"token": encoded_jwt}

#Create User Table
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

#Home
@app.route("/")
def home():
    return render_template('home.php')
#Login
@app.route("/login",methods=['GET','POST'])
def login():
    get_username = request.form.get('username')
    get_password = request.form.get('password')

    if request.method == 'POST':
    
        control_username = db.session.execute(text(f"SELECT username FROM user WHERE username = '{str(get_username)}'")).scalar()
        control_password = db.session.execute(text(f"SELECT password FROM user WHERE username = '{str(get_username)}'")).scalar()
        
    
        if check_password_hash(control_password,get_password):
            
            return f"logged in {token(get_username)}"

    
        elif not check_password_hash(control_password,get_password):
                BaseException("invalid password")
        
        if control_username is None:
            raise any("User not found")

    return render_template('login.php')
    
            
        
#Register      
@app.route("/register",methods=['GET','POST'])
def register():
    new_username = request.form.get('username')
    new_pass = request.form.get('password')
    
    #Existing Validation
    exist_username = db.session.query(User).filter_by(username=new_username).first()
    db.session.commit()
    

    if exist_username:
        raise TypeError("this username already exist")

    #Add User
    def include_user():
        if request.method == 'POST':
            
            hashed_pass = generate_password_hash(new_pass)

            new_user = User(
            username = new_username,
            password = hashed_pass)
        
            db.session.begin()
            db.session.add(new_user)
            db.session.commit()
            return f"Registered! welcome {new_user.username}"
        
    return render_template('register.php'), include_user()

    
if __name__ == "__main__":
    app.run(debug=True)