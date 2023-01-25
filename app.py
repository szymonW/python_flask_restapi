from flask import Flask, jsonify
from lib.helpers import create_games

app = Flask(__name__)


@app.route('/')
def index():
    names = ["player_1", "player_2", "player_3", "player_4"]
    return jsonify({'names': names,
                    'games': create_games(names)})


app.run(debug=True)
