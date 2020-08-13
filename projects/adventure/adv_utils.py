import copy
from collections import deque

# Scout object to explore/traverse map:
# Takes room object, not room id
class Scout:
    def __init__(self, room, world):
        self.room = room
        self.world = world
        self.compass = ["n", "e", "s", "w"]
        # facing: [0,1,2,3] = ["n", "e", "s", "w"]
        self.facing = 0
        # visited: set of room IDs
        self.visited = set([room.id])
        # steps: directions moved (e.g. "n", "e")
        self.steps = []
    def turn_left(self):
        self.facing = (self.facing - 1) % 4
    def turn_right(self):
        self.facing = (self.facing + 1) % 4
    def check_new_adjacent(self):
        for exit in self.room.get_exits():
            if self.room.get_room_in_direction(exit).id not in self.visited:
                return True
        return False
    def step_forward(self):
        direction = self.compass[self.facing]
        if direction in self.room.get_exits():
            self.steps.append(direction)
            self.room = self.room.get_room_in_direction(direction)
            self.visited.add(self.room.id)
    def move_direction(self, direction):
        if direction in self.room.get_exits():
            self.steps.append(direction)
            self.room = self.room.get_room_in_direction(direction)
            self.visited.add(self.room.id)
    def automap(self):
        while self.check_new_adjacent():
            self.turn_left()
            while self.compass[self.facing] not in self.room.get_exits():
                self.turn_right()
            self.step_forward()
    def nearest_new(self):
        checked = set()
        room_deque = deque([[self.room.id, []]])
        while (len(room_deque) > 0):
            this_state = room_deque.popleft()
            if this_state[0] not in self.visited:
                return this_state[1]
            else:
                room = self.world.rooms[this_state[0]]
                checked.add(room)
                for exit in room.get_exits():
                    if room.get_room_in_direction(exit) not in checked:
                        new_state = copy.deepcopy(this_state)
                        new_state[0] = room.get_room_in_direction(exit).id
                        new_state[1].append(exit)
                        room_deque.append(new_state)
        return []
    def go_to_new(self):
        for step in self.nearest_new():
            self.move_direction(step)

# Shortest route between rooms, not restricted to already-mapped:
def get_route(world, orig, dest):
    # world is world object, orig and dest are ROOM ID NUMBERS
    checked = set()
    # each deque item is a list of [room_id, [path to room_id]]
    room_deque = deque([[orig, []]])
    while (len(room_deque) > 0):
        this_state = room_deque.popleft()
        if this_state[0] == dest:
            return this_state[1]
        else:
            room = world.rooms[this_state[0]]
            checked.add(room)
            for exit in room.get_exits():
                if room.get_room_in_direction(exit) not in checked:
                    new_state = copy.deepcopy(this_state)
                    new_state[0] = room.get_room_in_direction(exit).id
                    new_state[1].append(exit)
                    room_deque.append(new_state)
    return None

# Shortest route to nearest unvisited room from given origin:
def go_to_new(world, orig, visited):
    checked = set()
    room_deque = deque([[orig, []]])
    while (len(room_deque) > 0):
        this_state = room_deque.popleft()
        if this_state[0] not in visited:
            return this_state[1]
        else:
            room = world.rooms[this_state[0]]
            checked.add(room)
            for exit in room.get_exits():
                if room.get_room_in_direction(exit) not in checked:
                    new_state = copy.deepcopy(this_state)
                    new_state[0] = room.get_room_in_direction(exit).id
                    new_state[1].append(exit)
                    room_deque.append(new_state)
    return None