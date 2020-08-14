from room import Room
from player import Player
from world import World
from scout import Scout

import datetime
import itertools
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

traversal_path = []

# print(datetime.datetime.now())
print(datetime.datetime.now())
compasses = itertools.permutations(["n", "e", "s", "w"])
scouts = [Scout(world.starting_room, world, i, list(j)) for i in (True, False) for j in compasses]
for scout in scouts:
    while len(scout.visited) < len(room_graph):
        # Transit continguous unexplored area:
        scout.automap()
        # Move to nearest unexplored room:
        scout.go_to_new()
traversals = sorted([scout.steps for scout in scouts], key=lambda traversal: len(traversal))
for scout in scouts:
    print(f"{len(scout.steps)} steps, {''.join(scout.compass)}, {scout.lefty}")

print(datetime.datetime.now())

traversal_path = traversals[0]

# print(datetime.datetime.now())

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
