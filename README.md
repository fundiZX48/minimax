# pyminimax
Simple Python 3 example of the minimax algorithm using a NetworkX graph

This example assumes you have NetworkX installed as part of your Python 3 distribution.

Using conda to install NetworkX:

    conda install -c anaconda networkx


run the example from the src folder:

    python src/minimax.py 


## Setting up a minimax graph

NetworkX is a great Python library for managing and traversing graph based structures.

Use G.add_node to add a node to the graph. Set *terminal* to *None* if the node is not a terminal value, otherwise set to a valid integer score:

```python
G.add_node("nodeName", terminal="valueOfTerminal")
```

Use G.add_edge to add an edge from a source node to a destination node:

```python
G.add_edge("sourceNode", "destinationNode")
```

## Todo

Add some visualisation for the graph. At the moment is it all pretty much pen and paper approach!

