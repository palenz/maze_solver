
id = '94a4dd75-8f32-4b64-ae9a-b27beb753e4a'
move_url = 'https://ponychallenge.trustpilot.com/pony-challenge/maze/'+id

move_params = {
  "direction": "east"
}

move_response = requests.post(move_url, json=move_params)
res = json.loads(response.text)

# ID value from the response is stored in the variable id.
id = res["maze_id"]

mar = False

def calculate_path(pony_position, end_point,)
while not(pony_position == end_point):


# possible_moves = check walls
#     if south: + width and run again
#     if north: - width and move again
#     if east: +1 and again
#     if west: -1