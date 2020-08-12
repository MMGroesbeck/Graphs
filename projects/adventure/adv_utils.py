import copy
from collections import deque

# Scout object to explore/traverse map:
# Takes room object, not room id
class Scout:
    def __init__(self, room):
        self.room = room
        self.compass = ["n", "e", "s", "w"]
        # facing: [0,1,2,3] = ["n", "e", "s", "w"]
        self.facing = 0
        self.visited = set([room.id])
        self.steps = []
    def turn_left(self):
        self.facing = (self.facing - 1) % 4
    def turn_right(self):
        self.facing = (self.facing + 1) % 4
    def step_forward(self):
        face = self.compass[self.facing]
        if face in self.room.get_exits():
            self.steps.append(face)
            self.room = self.room.get_room_in_direction(face)
            self.visited.add(self.room.id)

# Shortest route between rooms, not restricted to already-mapped:
def get_route(world, orig, dest):
    # world is world object, orig and dest are room id numbers
    checked = set()
    # each deque item is a list of [room_id, [path to room_id]]
    room_deque = deque([[orig, [orig]]])
    while (len(room_deque) > 0):
        this_state = room_deque.popleft()
        room = this_state[0]
        if room == dest:
            return this_state[1][1:]
        else:
            checked.add(room)
            routes = [world.rooms[room].n_to, world.rooms[room].e_to, world.rooms[room].s_to, world.rooms[room].w_to]
            for d in routes:
                if d is not None:
                    if d.id not in checked:
                        new_state = copy.deepcopy(this_state)
                        new_state[0] = d.id
                        new_state[1].append(d.id)
                        room_deque.append(new_state)
    return None