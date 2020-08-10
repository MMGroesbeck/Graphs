import datetime

from social import SocialGraph

social_graph = SocialGraph()

a = datetime.datetime.now()
social_graph.populate_graph(10000,50)

b = datetime.datetime.now()

paths = social_graph.get_all_social_paths(1)

c = datetime.datetime.now()

print(a)
print(b)
print(c)