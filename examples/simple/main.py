"""This module draw c preprocessing result using NetworkX drawing."""

def main():
    """draws a graph of c-preprocessed using danata-cpp-wrapper

    This example shows how to use danata-cpp-wrapper
    """

    import os
    import sys

    PROJECT_HOME = '%s/../..'%os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, PROJECT_HOME)

    import matplotlib
    import networkx as nx
    import matplotlib.pyplot as plt
    import danatacppwrapper as dcw
    import danata

    tree = dcw.read(sys.argv[1:]) 
    nx.draw_networkx(tree, danata.tree_layout(tree))
    plt.show()

if __name__ == "__main__":
    main()
