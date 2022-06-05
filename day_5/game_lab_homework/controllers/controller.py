from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game


@app.route('/')
def index():
    return render_template('index.html', title='Game')

@app.route('/<player1>/<player2>')
def get_var_from_url(player1, player2):
    player_1 = Player("Player One", player1)
    player_2 = Player("Player Two", player2)
    wins_game = Game.determine_winner(player_1, player_2)

    return render_template("winner.html", title="Winner takes all", wins_game=wins_game, player1=player_1, player2=player_2)


@app.route('/game')
def play_game():
    return render_template("game.html", title="WARNING! This is your amazing opporunity to take on Player2")

@app.route('/game', methods=["POST"])
def play_player2():
    name = request.form['name']
    choice = request.form['choice']
    player1 = Player(name, choice)
    player2 = Game.player2_as_computer()
    print(player2)
    wins_game = Game.determine_winner(player1, player2)
    return render_template("winner.html", title="Declared Winner", wins_game=wins_game, player1=player1, player2=player2)
