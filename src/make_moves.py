import requests
import json
from game import Game, url

# Returns true if domo is one or two steps ahead
def domo_ahead(game, first_move, second_move):
    next_block = position_calculator(game, first_move, game.pony_position)
    two_ahead = position_calculator(game, second_move, next_block)
    return game.domokun_position == next_block or game.domokun_position == two_ahead

def position_calculator(game, move, position):
    current_position = position
    if move == 'east':
        current_position += 1
    elif move == 'west':
        current_position -= 1
    elif move == 'south':
        current_position += game.width
    elif move == 'north':
        current_position -= game.width
    return current_position

# Returns a new list of moves with the last intersection list turned into a simple move
def last_intersection(moves):
    indexes = []
    new_moves = None
    for move in moves:
        if isinstance(move, list):
            indexes.append(moves.index(move))  
    i = max(indexes)
    new_moves = moves[:i]
    new_moves.append(moves[i][2])
    return new_moves

# Returns the block number of the last intersection
def last_intersection_position(moves):
    indexes = []
    new_pos = None
    for move in moves:
        if isinstance(move, list):
            indexes.append(moves.index(move))
    i = max(indexes)
    new_pos = moves[i][0]
    return new_pos

# Checks if there is a south wall
def south_wall(game, point):
    if (game.width*game.height) > point >= ((game.width*game.height)-game.width):
        return True
    else:
        south_block = point + game.width
        return 'north' in game.walls[south_block]

# Checks if there is an east wall
def east_wall(game, point):
    if (point+1) % game.width == 0:
        return True
    else:
        east_block = point + 1
        return 'west' in game.walls[east_block]
    
# Returns the available moves for any given block number
def available_moves(game, position):
    moves = []
    if not('north' in game.walls[position]):
        moves.append('north')
    if not('west' in game.walls[position]):
        moves.append('west')
    if not(south_wall(game, position)):
        moves.append('south')
    if not(east_wall(game, position)):
        moves.append('east')
    return moves

# Calculates the opposite move
def opposite(direction):
    if direction == 'north':
        return 'south'
    elif direction == 'south':
        return 'north'
    elif direction == 'east':
        return 'west'
    elif direction == 'west':
        return 'east'

# Formats the final path to remove intersection lists
def clean_path(path):
    clean_path = path
    for move in clean_path:
        if type(move) == list:
            to_insert = move[1]
            i = clean_path.index(move)
            clean_path.remove(move)
            clean_path.insert(i, to_insert)
    return clean_path

# Tries possible options until it finds the path to the exit point
# Path will look like this [[13, right, left], north, south, south]
def find_path(game):
    path = []
    position = game.pony_position

    while position != game.end_point_position:

        if len(path) == 0:
            start_moves = available_moves(game, position)
            new_position = position_calculator(game, start_moves[0], position)
            path.append([position])
            path[0].extend(start_moves)
            position = new_position

        elif len(available_moves(game, position)) == 2:
            if type(path[-1]) == str:
                last_move = path[-1]
            elif type(path[-1]) == list:
                last_move = path[-1][1]
            lm_opposite = opposite(last_move)
            moves = available_moves(game, position)
            moves.remove(lm_opposite)
            new_position = position_calculator(game, moves[0], position)
            path.append(moves[0])
            position = new_position

        elif len(available_moves(game, position)) == 3:
            if type(path[-1]) == str:
                last_move = path[-1]
            elif type(path[-1]) == list:
                last_move = path[-1][1]
            lm_opposite = opposite(last_move)
            moves = available_moves(game, position)
            moves.remove(lm_opposite)
            new_position = position_calculator(game, moves[0], position)
            path.append([position])
            path[-1].extend(moves)
            position = new_position          

        elif len(available_moves(game, position)) == 1:
            last_int_position = last_intersection_position(path)
            new_path = last_intersection(path)
            path = new_path
            position = position_calculator(game, new_path[-1], last_int_position)     

    return clean_path(path) 

# Makes the next move post request (also added game.print_game() to view the game in the terminal)
def make_move(game, move):
    game.print_game()
    move_params = {
        "direction": move
        }
    res = requests.post(url + "/" + game.id, json=move_params)
    move_response = json.loads(res.text)
    game.status = move_response['state']
    game.status_message = move_response['state-result']

# Follows the path and prints the end result. 
def solve_maze(game):
    if game.status == 'Active':
        vpath = find_path(game)
        for index, move in enumerate(vpath):
            i_next_move = index + 1
            i_previous_move = index - 1
            previous_move = vpath[i_previous_move]
            run = opposite(previous_move)
            next_move = vpath[i_next_move]
            if game.status == 'over':
                break
            if domo_ahead(game, move, next_move):
                # domo_threat = True
                make_move(game, run)
            else:
                # if domo_threat == True:
                #     make_move(game, previous_move)
                #     make_move(game, move)
                #     domo_threat = False
                # else:
                    make_move(game, move)

        print(game.status_message)
    elif game.status == 'over' or game.status == 'won':
        print(game.status_message)



# Initialise and call the create_game() and solve_maze() functions below

# Example
game1 = Game("Applejack", 15, 15, 1)
game1.create_game()
solve_maze(game1)


    



