import copy
from collections import deque

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
            return this_state[1]
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