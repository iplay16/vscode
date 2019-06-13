import sys
def RecurMatrixChain(P):
    if not P:
        return
    minval=sys.minisize()
    for i,x in enumerate(P):
        temp=RecurMatrixChain(P[i:])+RecurMatrixChain(P[:i])
        if temp<minval:
            minval=temp         
