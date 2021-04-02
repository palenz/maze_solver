import requests
import json

url = "https://ponychallenge.trustpilot.com/pony-challenge/maze"

# Edit the params below and run this file to create a new maze
maze_params = {
  "maze-width": 15,
  "maze-height": 15,
  "maze-player-name": "Applejack",
  "difficulty": 2
}

# Request is sent with the body.
response = requests.post(url, json=maze_params)

# Response is parsed and stored in a dictionary, so we can access parts of the response.
res = json.loads(response.text)

# ID value from the response is stored in the variable id.
maze_id = res["maze_id"]

print(maze_id)



