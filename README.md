# TrustPilot's Pony Challenge
### _by Juan Palenzuela_


The goal of the challenge is to create a program that drives the pony to the
end point while avoiding Domokun.

The Game class contains the necessary methods to initialise a game. To create a new game, the first step is to create a new game object. You will need a [valid My Little Pony name][1], maze height & width and difficulty level. More information on the [challenge's documentation page][2].

The second step is to go to make_moves.py and call the `create_game()` method on the new game object. This method makes a POST request to create a new game, and it will also call the `get_info()` method, which will populate most of the remaining empty attributes.


## Solving the maze

The `solve_maze()` function takes in a game object as its only argument. It then calls `explore_path()`, which explores the maze until it finds the path to the end point.

Every time a move is made, the game will be printed. This helps visualise the movements from a terminal. The result will be printed too.

There is some logic inside `solve_maze()` (lines 160-177) to help the pony avoid Domokun. The idea is that if Domo is nearby, the pony will take one step back where it came from and then continue on its path if Domo is no longer on the way.

## About the maze & solving strategy

- There seems to always be just one path to the endpoint, which means that there are no loops. There is no "shortest" path.
- The positions are indented and they are measured by the block left to right and top to bottom. For example, if the pony’s position is 15 in a 15x15 game, the pony is in the first column left to right, on the second row top to bottom.
- The “data” list in the JSON response after requesting game information contains information on each block. To find walkable directions, one must calculate if there are south walls or east walls: a south wall is the north wall for another cell, etc.


[1]: <https://mlp.fandom.com/wiki/Characters>
[2]: <https://ponychallenge.trustpilot.com/api-docs/index.html#/pony-challenge>
  
