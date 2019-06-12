from typing import List
from typing import NewType

class gametree:
    def __init__(self,flag):
        self.flag=flag #1 mean max -1 means min
        self.nextstep=[] #:List[gamenodetype]
        self.position:[int]=[]
        self.val=-1
        self.gametreeval=-1

    def put():


def countval(gametree):
    gametree.val=countfp()
    for next in gametree.nextstep:
        countval(gametree)

def countgametreeval(gametree,flag):
    minval=-1
    maxval=-1
    if flag==1:
        for next in gametree.nextstep:
            minval=min(minval,next)
        gametree.gametreeval=minval
    if flag==-1:
        for next in gametree.nextstep:
            maxval=min(maxval,next)
        gametree.gametreeval=maxval
    
    for next in gametree.nextstep:
        countgametreeval(next,-flag)
g=gametree()
