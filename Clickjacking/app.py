from flask import Flask, render_template, request, session, flash
from flask_migrate import Migrate
from models import db, Garena, Config

app = Flask(__name__)
app.config.from_object(Config)

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Garena.query.filter_by(username=username, password=password).first()
        if user:
            pass  # Tùy chỉnh hành động khi login thành công
        else:
            new_user = Garena(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        existing_user = Garena.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists.", "danger")
        else:
            new_user = Garena(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful!", "success")
            return render_template('login.html')
    return render_template('register.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
