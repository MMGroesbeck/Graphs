from room import Room
from player import Player
from world import World
from adv_utils import get_route, Scout

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# Version 1: traveling blind
# Algorithm refers only to rooms adjacent to known rooms
# Keep dict or set (x) of known rooms with unknown adjacent rooms
# Start facing north
# While not all rooms discovered:
## If unknown room ahead:
### Step forward
### Add current room to known graph
### Turn left
## Else:
### turn right until unknown room ahead or have turned 4 times
### If no adjacent unknown rooms:
#### Follow shortest path to a room in dict/set (x)
# Additional details:
## Keep track of coordinates relative to starting point:
### If adjacent rooms with a connection have been visited, fill in connections
## room.x and room.y are coordinates
### going east increases x, going north increases y
### so keep a dict of rooms by (x,y)

# Version 2: use your map
# Keep dict/set (x) of rooms with unvisited adjacents
## True if visited *or no room*, False if unvisited
# Follow step-and-turn as above
## At each step, update (x) as well as visited set and path
# If no adjacent unvisited rooms, use world object graph
## Find shortest path to an unvisited room
traversal_path = []
scout = Scout(world.starting_room, world)
while len(scout.visited) < len(room_graph):
    scout.automap()
    scout.go_to_new()
traversal_path = scout.steps

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
