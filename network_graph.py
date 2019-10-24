import matplotlib.pyplot as plt
import networkx as nx
from link_crawler import Crawler


page_link = "https://en.wikipedia.org/wiki/British_telephone_socket"
depth_required = 3

test = Crawler(page_link, depth_required)
results = test.link_grabber()
# print(results)
# print(len(results))

print(results)

G = nx.Graph()

G.add_nodes_from(results[1]) #each node must be just one item. So in this case, the first item from each tuple
G.add_edges_from(results) #results is a list of tuples, so already in the correct format

nx.draw(G)
plt.savefig("simple_path.png") # save as png
plt.show() # display

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())



