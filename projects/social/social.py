import random
import copy

from collections import deque

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        letters = "abcdefghijklmnopqrstuvwxyz"
        for i in range(num_users):
            self.add_user("".join(random.sample(letters, 8)))

        # Create friendships
        total_friendships = (num_users * avg_friendships)//2
        user_ids = [i for i in range(1,num_users + 1)]
        links = [random.choice(user_ids) for i in range(total_friendships)]
        for link in links:
            j = random.choice(user_ids)
            while j == link or j in self.friendships[link]:
                j = random.choice(user_ids)
            self.add_friendship(link, j)
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        user_deque = deque([[user_id, [user_id]]])
        while len(user_deque) > 0:
            this_state = user_deque.popleft()
            if this_state[0] not in visited:
                visited[this_state[0]] = this_state[1]
                for friend in self.friendships[this_state[0]]:
                    new_state = copy.deepcopy(this_state)
                    new_state[0] = friend
                    new_state[1].append(friend)
                    user_deque.append(new_state)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
