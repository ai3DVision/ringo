PlotKCoreEdges
''''''''''''''

.. function:: PlotKCoreEdges(Graph, FNmPref, DescStr)

Plots the k-core edge-size distribution: core k vs. number of edges in k-core. The function creates three new files: 1) coreEdges.<*FNmPref*>.plt (the commands used to create the plot), 2) coreEdges.<*FNPref*>.png (the plot), and 3) coreEdges.<*FNmPref*>.tab (the plotting data).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *FNmPref*: string (input)
    A string representing the preferred output file name.

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to plot the k-core edge-size distribution for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotKCoreEdges(Graph, "example", "Directed graph - k-core edges")
    
    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotKCoreEdgees(UGraph, "example", "Undirected graph - k-core edges")

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotKCoreEdges(Network, "example", "Network - k-core edges")


