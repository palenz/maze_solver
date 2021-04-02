import requests
import json

id = '6026e6c5-696b-4d58-941b-a90a9740ef00'
url = 'https://ponychallenge.trustpilot.com/pony-challenge/maze/'+id

def make_move(move):
    move_params = {
        "direction": move
        }
    res = requests.post(url, json=move_params)
    move_response = json.loads(res.text)
    state_result = [move_response['state'], move_response['state-result']]
    return state_result

def calculate_path(game):
#     while not(game.pony_position == game.end_point):


print(make_move("east"))

# possible_moves = check walls
#     if south: + width and run again
#     if north: - width and move again
#     if east: +1 and again
#     if west: -1