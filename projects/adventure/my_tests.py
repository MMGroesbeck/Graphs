from room import Room
from world import World
from adv_utils import get_route, Scout
from ast import literal_eval

world = World()

map_file = "maps/test_loop_fork.txt"
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# scout = Scout(world.starting_room, world)
# print("v: ", scout.visited)
# print(scout.room)

world.print_rooms()