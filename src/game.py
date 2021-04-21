import requests
import json

url = "https://ponychallenge.trustpilot.com/pony-challenge/maze"

# Status should be None
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
      self.status = 'active'
      self.victory_path = None
      self.status_message = None
      self.domo_threat = False

    def get_info(self):
      info_url = url + '/' + self.id
      res = requests.get(info_url)
      parsed_res = json.loads(res.text)

      self.pony_position = parsed_res['pony'][0]
      self.domokun_position = parsed_res['domokun'][0]
      self.end_point_position = parsed_res['end-point'][0]
      self.walls = parsed_res['data']
      self.status = parsed_res['game-state']['state']
      self.status_message = parsed_res['game-state']['state-result']

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

    def print_game(self):
      res_print = requests.get(url + "/" + self.id + "/print")
      print(res_print.text)






