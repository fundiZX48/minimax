# pyminimax
Simple Python 3 example of the minimax algorithm using a NetworkX graph

This example assumes you have NetworkX installed as part of your Python 3 distribution.

Using conda to install NetworkX:

    conda install -c anaconda networkx

or if you prefer pip:

    pip install networkx

run the example from the src folder:

    python src/minimax.py 


## Setting up a minimax graph

NetworkX is a great Python library for managing and traversing graph based structures.

Use *G.add_node()* to add a node to the graph. Set *terminal* to *None* if the node is not a terminal value, otherwise set to a valid integer or float score:

```python
G.add_node("nodeName", terminal=int_or_float_value)
```

Use *G.add_edge()* to add an edge from a source node to a destination node:

```python
G.add_edge("sourceNode", "destinationNode")
```

## Visualizing the graph

Check the correctness of your graph by visualizing it. You will require pydot and Graphviz. If running on Ubuntu/Linux you require Graphviz:

    sudo apt install graphviz

And pydot Python installation using pip:

    pip install pydot

(conda does not seem to support pydot and Python 3)

And the Python code to accomplish this:

```python
    p = nx.drawing.nx_pydot.to_pydot(G)
    p.write_png('output_filename.png')
```

And below is a graph example from the *complex_tree()* function: 

![complex_tree](/src/complex_tree.png)

For sake of clarity and to highlight terminal nodes in the graph visualization, I have annotated the *add_node()* methods like this:

```python
G.add_node("nodeName=terminal", terminal=int_or_float_value)
```

That is add the terminal value to the name of the node. Note, *add_edge()* should also correspond to the annotated node name.

