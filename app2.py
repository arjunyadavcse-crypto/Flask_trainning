from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#database configuration code

# Define Database URI: mysql+pymysql://username:password@host/database_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("Arjun")
# Initialize SQLAlchemy
db = SQLAlchemy(app)
  # databaase model
class user(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    email = db.Column(db.String(80))
    phone_num = db.Column(db.String(80))
    msg = db.Column(db.String(80))
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    #run the Flask app
    app.run(debug=True)