#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
import itertools
import heapq
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wfdict={}
        for s in words:
            if s in wfdict.keys():
                wfdict[s]+=wfdict[s]
            else:
                wfdict[s]=1
        list0=list(wfdict.items())
        heapq.heapify(list0)
        list1=heapq.nlargest(n=k+10,iterable=list0,key=lambda x:x[1])
        # list0 = sorted(wfdict.items(),key=lambda x:x[0])
        print([i for i,_ in itertools.islice(list1,k+10)])
        list1 = sorted(list1,key=lambda x:x[0])
        list1 = sorted(list1,key=lambda x:x[1],reverse=True)
        return [i for i,_ in itertools.islice(list1,k)]
# import tools
# tools.runTest(["i", "love", "leetcode", "i", "love", "coding"],2)
if __name__=='__main__':
    l=["i", "love", "leetcode", "i", "love", "coding"]
    num=int(2)
    x=Solution().topKFrequent(l,num)
    print(x)
