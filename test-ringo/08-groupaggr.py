import os
import resource
import sys
import time

sys.path.append("../utils")
sys.path.append("../ringo-engine-python")
import ringo
import snap
import testutils

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print """Usage: """ + sys.argv[0] + """ <srcfile>
        srcfile: posts.tsv file from StackOverflow dataset"""
        sys.exit(1)

    srcfile = sys.argv[1]
    
    ringo = ringo.Ringo()
    
    t = testutils.Timer()
    r = testutils.Resource()

    S = [("Id", "int"), ("OwnerUserId", "int"), ("AcceptedAnswerId", "int"), ("CreationDate", "string"), ("Score", "int")]
    table = ringo.LoadTableTSV(S, srcfile)
    t.show("load text")
    r.show("__loadtext__")
    
    V = snap.TStrV()
    V.Add("OwnerUserId")
    table.Aggregate(V, snap.aaSum, "Score", "Sum")

    t.show("group_aggregate")
    r.show("__group_aggregate__")
