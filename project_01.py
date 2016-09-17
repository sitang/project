from pprint import pprint

# Defining a player
player_id = 1 # id code unique to each player (integer)
player_name = '' # entered name of the player (string)
time_played = float() # number of time played the game in minutes (float)
player_pokemon = {} # the player's captured pokemon (dictionary)
gyms_visited = [] # ids of the gyms that a player has visited (list)

# Defining "gym" locations
gym_loc = ['reddit.com', 'amazon.com', 'twitter.com', 'linkedin.com', 
'ebay.com', 'netflix.com', 'udacity.com', 'stackoverflow.com', 'github.com', 'quora.com']
#print gym_loc

gyms_visited.append(gym_loc[0])
gyms_visited.append(gym_loc[1])
#print gyms_visited

# Create a pokedex
pokemon_id = int() # pokemon_id : unique identifier for each pokemon (integer)
name = '' # name : the name of the pokemon (string)
pokemon_type = '' # type : the category of pokemon (string)
hp = int() # hp : base hitpoints (integer)
attack = int() # attack : base attack (integer)
defense = int() # defense : base defense (integer)
special_attack = int() # special_attack : base special attack (integer)
sepcial_defense = int() # special_defense : base sepecial defense (integer)
speed = int() # speed : base speed (integer)

pokemon_dict = {
	1: {
		'name': 'charmander', 'type': 'fire', 'hp': 15, 'attack': 30, 
		'defense': 20, 'special_attack': 40, 'special_defense': 30, 'speed': 25
		},
	2: {
		'name': 'squirtle', 'type': 'water', 'hp': 10, 'attack': 10, 
		'defense':20, 'special_attack': 20, 'special_defense': 30, 'speed': 25
		},
	3: {'name': 'bulbasaur', 'type': 'poison', 'hp': 20, 'attack':25, 
		'defense': 10, 'special_attack': 30, 'special_defense': 15, 'speed': 15
		}
}
#print pokemon_dict

# Create a data structure for players
# 4.1
player_dict = {player_id: {
				'player_name': player_name,
				'player_pokemon': {},
				'time_played': time_played,
				'gyms_visited': []
				}
			}
player_dict[player_id]['player_name'] = 'Ash'
player_dict[player_id]['gyms_visited'] = gyms_visited

# 4.2
player_id += 1
player_dict[player_id] = player_dict.get(player_id, {})
player_dict[player_id]['player_name'] = 'pikachu'
player_dict[player_id]['gyms_visited'] = [gym_loc[7], gym_loc[8]]
#print player_dict

# Add captured pokemon for each player
player_dict[1]['player_pokemon'] = {2: pokemon_dict[2]}
player_dict[2]['player_pokemon'] = {1: pokemon_dict[1], 3: pokemon_dict[3]}
#print player_dict

# What gyms have players visited?
for gym in gym_loc:
	for player in player_dict:
		if filter(lambda x: x == gym, player_dict[player]['gyms_visited']):
			print player_dict[player]['player_name'] + ' has visited ' + gym +'.'
		else:
			pass

# Calculate player "power"
def play_power(player_dict, pokemon_dict, player_id):
	attack = [i['attack'] for i in player_dict[player_id]['player_pokemon'].values()]
	defense = [i['defense'] for i in player_dict[player_id]['player_pokemon'].values()]
	power = sum(attack + defense)
	print player_dict[player_id]['player_name'] + "'s power is", power
	print power

# Load a pokedex file containing all the pokemon

# Code to read in pokedex info
# ['PokedexNumber', 'Name', 'Type', 'Total', 'HP', 'Attack', 'Defense', 'SpecialAttack', 'SpecialDefense', 'Speed']
# [1.0, 'Bulbasaur', 'GrassPoison', 318.0, 45.0, 49.0, 49.0, 65.0, 65.0, 45.0]
# [2.0, 'Ivysaur', 'GrassPoison', 405.0, 60.0, 62.0, 63.0, 80.0, 80.0, 60.0]
raw_pd = ''
pokedex_file = 'https://github.com/ga-students/DSI-SF-3/blob/master/datasets/pokemon/pokedex_basic.csv'
with open(pokedex_file, 'r') as f:
    raw_pd = f.read()
raw_pd.split('\n')
