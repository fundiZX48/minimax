import networkx as nx


def minimax(G, n):
    """Perform minimax from node n on a NetworkX graph G.
    Assume node n is a maximiser node.
    """

    maxplayer = True
    minplayer = False

    def _minimax(G, n, player):
        # Base case, terminal node found
        if G.node[n]["terminal"]:
            return G.node[n]["terminal"]
        
        if player == maxplayer:
            bestv = float("-inf")
            for child in G.successors(n):
                v = _minimax(G, child, minplayer)
                bestv = max(bestv, v)
        else:
            bestv = float("inf")
            for child in G.successors(n):
                v = _minimax(G, child, maxplayer)
                bestv = min(bestv, v)
        return bestv

    # Find the best first move from the given node
    # Assume given node n is a maximiser node.
    best_move = None
    bestv = float("-inf")
    for child in G.successors(n):
        v = _minimax(G, child, minplayer)
        if v > bestv:
            best_move = child
            bestv = v
    return (best_move, v)


def simple_tree():
    G = nx.DiGraph()

    G.add_node("root", terminal=None)
    G.add_node("a", terminal=-1)
    G.add_node("b", terminal=None)
    G.add_node("c", terminal=3)

    G.add_edge("root", "a")
    G.add_edge("root", "b")
    G.add_edge("b", "c")

    print("Best path to take in simple_tree():", minimax(G, n="root"))


def complex_tree():
    # Example taken from:
    # http://web.cs.ucla.edu/~rosen/161/notes/minimax.html
    G = nx.DiGraph()

    G.add_node("root", terminal=None)
    G.add_node("a", terminal=None)
    G.add_node("b", terminal=None)
    G.add_node("c", terminal=None)
    G.add_node("d", terminal=7)
    G.add_node("e", terminal=3)
    G.add_node("f", terminal=15)
    G.add_node("g", terminal=1)
    G.add_node("h", terminal=12)
    G.add_node("i", terminal=20)
    G.add_node("j", terminal=22)

    G.add_edge("root", "a")
    G.add_edge("root", "b")
    G.add_edge("root", "c")

    G.add_edge("a", "d")
    G.add_edge("a", "e")

    G.add_edge("b", "f")

    G.add_edge("c", "g")
    G.add_edge("c", "h")
    G.add_edge("c", "i")
    G.add_edge("c", "j")

    print("Best path to take in complex_tree():", minimax(G, n="root"))


def main():
    simple_tree()
    complex_tree()


if __name__ == "__main__":
    main()
