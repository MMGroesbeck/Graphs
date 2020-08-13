import copy
from collections import deque

# Scout object to explore/traverse map:
# Takes room object, not room id
class Scout:
    def __init__(self, room, world, lefty=True):
        self.room = room
        self.world = world
        self.lefty = lefty
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
        # Returns True if any adjacent rooms have not been visited
        for exit in self.room.get_exits():
            if self.room.get_room_in_direction(exit).id not in self.visited:
                return True
        return False
    def step_forward(self):
        # Adds step to path, moves in facing direction, updates room.
        direction = self.compass[self.facing]
        if direction in self.room.get_exits():
            self.steps.append(direction)
            self.room = self.room.get_room_in_direction(direction)
            self.visited.add(self.room.id)
    def move_direction(self, direction):
        # Moves without changing facing direction
        if direction in self.room.get_exits():
            self.steps.append(direction)
            self.room = self.room.get_room_in_direction(direction)
            self.visited.add(self.room.id)
    def branch_eval(self, room):
        checked = set([room.id])
        branch_deque = deque([room.id])
        while len(branch_deque) > 0:
            this_room_id = branch_deque.popleft()
            this_room = self.world.rooms[this_room_id]
            if this_room_id not in checked and this_room_id not in self.visited:
                checked.add(this_room_id)
            for exit in this_room.get_exits():
                new_room_id = this_room.get_room_in_direction(exit).id
                if new_room_id not in checked and new_room_id not in self.visited:
                    branch_deque.append(new_room_id)
        return len(checked)
    def automap(self):
        step_tens = 1
        while self.check_new_adjacent():
            if self.lefty:
                self.turn_left()
            else:
                self.turn_right()
            # while self.compass[self.facing] not in self.room.get_exits():
            #     if self.lefty:
            #         self.turn_right()
            #     else:
            #         self.turn_left()
            # self.step_forward()
            branches = {}
            for exit in self.room.get_exits():
                print(f"R: {self.room.id}, e: {exit}")
                branches[exit] = self.branch_eval(self.room.get_room_in_direction(exit))
            print(branches)
            if self.lefty:
                rel_dir = [0,1,2]
            else:
                rel_dir = [0,-1,-2]
            shortest = None
            for d in rel_dir:
                this_dir = self.compass[(self.facing + d) % 4]
                print(f"t_d: {this_dir}, s.f: {(self.facing + d) % 4}")
                print(f"Sh: {shortest}")
                if this_dir in branches:
                    print("In branches")
                    if shortest is not None:
                        if branches[this_dir] < branches[shortest]:
                            shortest = this_dir
                    else:
                        shortest = this_dir
            self.facing = self.compass.index(shortest)
            self.step_forward
    def nearest_new(self):
        # Returns path to nearest unvisited room
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
        facing = self.compass.index(self.steps[-1])
# End Scout object declaration

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