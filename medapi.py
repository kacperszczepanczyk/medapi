from flask import Flask
from flask_restful import Resource, Api
from iron_cache import *
from Parser import *
from Memcache import Memcache


app: Flask = Flask(__name__)
api = Api(app)
cache = IronCache()
memcache = Memcache()
parser = Parser()


class OnlinePlayers(Resource):
    def get(self, world):
       # item = cache.get(cache="online_players", key=str(world))
       # return item.value
        item = memcache.cache.get(world)
        return item


class Highscores(Resource):
    def get(self, world, profession):
        #item = cache.get(cache="highscores", key=world + '_' + profession)
        # return item.value
        item = memcache.cache.get('highscores_' + world + '_' + profession)
        return item


class PlayerInfo(Resource):
    def get(self, name):
        return json.dumps(parser.get_player_info(name))


class PlayerExists(Resource):
    def get(self, name):
        return parser.player_exists(name)


api.add_resource(OnlinePlayers, '/online_players/<world>')
api.add_resource(Highscores, '/highscores/<world>/<profession>')
api.add_resource(PlayerInfo, '/player_info/<name>')
api.add_resource(PlayerExists, '/player_exists/<name>')

if __name__ == '__main__':
    app.run(port='')
