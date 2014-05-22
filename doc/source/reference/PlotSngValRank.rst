PlotSngValRank
''''''''''''''

.. function:: PlotSngValRank(Graph, SngVals, FNmPref, DescStr)

Plots the rank distribution of singular values of the Graph adjacency matrix. Plots first *SngVals* values. The function creates three new files: 1) sngVal.<*FNmPref*>.plt (the commands used to create the plot), 2) sngVal.<*FNPref*>.png (the plot), and 3) sngVal.<*FNmPref*>.tab (the plotting data).

Parameters:

- *Graph*: directed graph (input)
    A Snap.py directed graph.

- *SngVals*: int (input)
    Number of largest singular values to plot.

- *FNmPref*: string (input)
    File name preference for the plotted graph.

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to plot the rank distribution of singular values of the Graph adjacency matrix for :class:`TNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotSngValRank(Graph, 100, "filename", "Singular Value Distribution")
