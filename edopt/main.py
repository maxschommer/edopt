import networkx as nx
import matplotlib.pyplot as plt


class Node():
    """This is the base class for a nx node

    It has basic electrical properties like
        Voltage (All nodes have voltage)
        Charge (Pins can collect charge, like capacitors)

    Nodes compute functions as well, which based on the
    edges the node is connected to, 
    """
    pass


class Wire():
    """This is the base class for a nx edge

    It has basic electrical properties like
        Voltage
        Current
    """
    pass


class Pin(Node):
    """A pin is a node
    """
    pass


class ComponentCore(Node):
    """The "core" of a component is a node. It is surrounded by other nodes
    which are pins.
    """
    pass


class Component(nx.Graph):
    """A component is a graph
    """
    # An "empty" component is a graph with 1 node (ComponentCore), itself
    pass


class Sheet(nx.Graph):
    """A sheet is just a graph with a draw function and some other stuff
    """
    pass


class Schematic(nx.Graph):
    """A schematic is a graph which contains many sheets, etc.
    """
    pass


n = Node()

G = nx.Graph()
G.add_node(n)
print(G.nodes)
# G.add_nodes_from([2, 3])
# G.add_edge(1, 2)
# G.add_edge(1, 3)
# G.add_edge(2, 3)
# nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue",
#         node_shape="s", alpha=0.5, linewidths=40)
# plt.show()
