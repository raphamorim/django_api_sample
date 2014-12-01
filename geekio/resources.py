import json

from geekio import api
from flask.ext import restful

game_json = 'geekio/data/game/data.json'

class Game(restful.Resource):
    def get(self):
        with open(game_json) as data:
            return json.load(data)

if __name__ == 'geekio.resources':
    api.add_resource(Game, '/game/')