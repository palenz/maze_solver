import requests
import json

url = "https://ponychallenge.trustpilot.com/pony-challenge/maze"


class Game:
    def __init__(self, pony_name, width, height, difficulty):
      self.pony_name = pony_name
      self.width = width
      self.height = height
      self.difficulty = difficulty
      self.id = None
      self.pony_position = None
      self.domokun_position = None
      self.end_point_position = None
      self.walls = None
      self.game_state = None

    def get_info(self):
      info_url = url + '/' + self.id
      res = requests.get(info_url)
      parsed_res = json.loads(res.text)

      self.pony_position = parsed_res['pony'][0]
      self.domokun_position = parsed_res['domokun'][0]
      self.end_point_position = parsed_res['end-point'][0]
      self.walls = parsed_res['data']
      self.game_state = parsed_res['game-state']

      # print(game1.pony_position)
      # print(game1.walls)
      # print(game1.end_point_position)
      # print(game1.game_state)


    def create_game(self):
      game_params = {
        "maze-width": self.width,
        "maze-height": self.height,
        "maze-player-name": self.pony_name,
        "difficulty": self.difficulty
      }
      res = requests.post(url, json=game_params)
      self.id = json.loads(res.text)['maze_id']
      if self.id:
        self.get_info()


# game1 = Game('Applejack', 15, 15, 2)
# game1.create_game()

# print(game1.id)





