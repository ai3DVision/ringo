GetSngVec
'''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetSngVec(Graph, SngVecs, SngValV, LeftSV, RightSV)

.. note::

    This function is not yet supported.

Computes the singular values and left and right singular vectors of the adjacency matrix representing a directed Graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- SngVecs: int (input)
    The number of singular values/vectors to compute

- SngValV: TFltV (output)
    Computed singular values stored as a vector of floats

- LeftSV: TVec<TFltV> (output)
    Computed left singular vectors stored as a vector of vectors of floats

- RightSV: TVec<TFltV> (output)
    Computed right singular vectors stored as a vector of vectors of floats
    
Return value:

- None

The following example shows how to fetch the in-degrees for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    SngVecs = 5
    SngValV = snap.TFltV()
    LeftSV = snap.TVec(snap.TFltV())
    RightSV = snap.TVec(snap.TFltV())
    snap.GetSngVec(Graph, SngVecs, SngValV, LeftSV, RightSV)
    for value in SngValV:
        print("Singular value: %f" % value)
    for vector in LeftSV:
        for value in vector:
            print("Left Singular Vector Value %f" % value)
    for vector in RightSV:
        for value in vector:
            print("Right Singular Vector Value %f" % value)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    SngVecs = 5
    SngValV = snap.TFltV()
    LeftSV = snap.TVec(snap.TFltV())
    RightSV = snap.TVec(snap.TFltV())
    snap.GetSngVec(Graph, SngVecs, SngValV, LeftSV, RightSV)
    for value in SngValV:
        print("Singular value: %f" % value)
    for vector in LeftSV:
        for value in vector:
            print("Left Singular Vector Value %f" % value)
    for vector in RightSV:
        for value in vector:
            print("Right Singular Vector Value %f" % value)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    SngVecs = 5
    SngValV = snap.TFltV()
    LeftSV = snap.TVec(snap.TFltV())
    RightSV = snap.TVec(snap.TFltV())
    snap.GetSngVec(Graph, SngVecs, SngValV, LeftSV, RightSV)
    for value in SngValV:
        print("Singular value: %f" % value)
    for vector in LeftSV:
        for value in vector:
            print("Left Singular Vector Value %f" % value)
    for vector in RightSV:
        for value in vector:
            print("Right Singular Vector Value %f" % value)
