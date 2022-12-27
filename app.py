"""Blogly application."""

from flask import Flask,request,redirect,render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db,User

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:secret@localhost:5432/bloggy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']='SECRET'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)
# db.create_all()

@app.route('/')
def home():
    """show list of all users"""
    users = User.query.all()
    return render_template('home.html', users= users)

@app.route('/', methods=['POST'])
def add_user():
    first= request.form['F']
    last = request.form['L']
    source= request.form['image']
    user=User(first_name=first, last_name= last,image_url= source or None )
    db.session.add(user)
    db.session.commit()
    return redirect(f"/{user.id}")


@app.route('/<int:user_id>')
def show_user(user_id):
    user=User.query.get_or_404(user_id)
    return render_template("detail.html", user= user)

@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    """show details about a single user"""
    user= User.query.get_or_404(user_id)
    return render_template('edit.html',user = user)

@app.route('/edit/<int:user_id>', methods=['POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['F']
    user.last_name= request.form['L']
    user.image_url = request.form['image']

    db.session.add(user)
    db.session.commit()

    return redirect('/')

@app.route('/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')