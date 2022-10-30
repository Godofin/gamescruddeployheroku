from flask import render_template, request, redirect, flash, url_for
from gamelib import app, db
from models import Games

@app.route('/')
def index():
    gameList = Games.query.order_by(Games.id)
    return render_template('list.html', title='Games', games=gameList)

@app.route('/newgame')
def newgame():
    return render_template('newGame.html', title='New Game')

@app.route('/editgame/{{ <int:id> }}')
def editgame(id):
    game = Games.query.filter_by(id=id).first()
    return render_template('edit.html', title='Edit Game', game=game)

@app.route('/create', methods=['POST',])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    asin = request.form['asin']
    language = request.form['language']

    game = Games.query.filter_by(name=name).first()
    if game:
        flash('Game does exists')
        return redirect(url_for('index'))

    new_game = Games(name=name, category=category, console=console, asin=asin, language=language)
    db.session.add(new_game)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/update', methods=['POST',])
def update():
    game = Games.query.filter_by(id=request.form['id']).first()
    game.name = request.form['name']
    game.category = request.form['category']
    game.console = request.form['console']
    game.asin = request.form['asin']
    game.language = request.form['language']

    db.session.add(game)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    Games.query.filter_by(id=id).delete()
    db.session.commit()
    flash("The game has deleted with sucessfull")
    return redirect(url_for('index'))