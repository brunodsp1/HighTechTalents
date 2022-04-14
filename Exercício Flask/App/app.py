from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pessoas.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class pessoas(db.Model):
    id = db.Column('pessoa_id', db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(50))
    telefone = db.Column(db.Integer, unique=True)
    nascimento = db.Column(db.String(10))

    def __init__(self, nome, email, telefone, nascimento):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nascimento = nascimento


@app.route('/')
def show_all():
    return render_template('show_all.html', pessoas=pessoas.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['email'] or not request.form['nascimento']:
            flash('Por favor preencha todos os campos.', 'error')
        else:
            pessoa = pessoas(request.form['nome'], request.form['email'],
                             request.form['telefone'], request.form['nascimento'])

            db.session.add(pessoa)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
