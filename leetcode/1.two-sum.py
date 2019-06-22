#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        ha=hashtable(length)
        for i,x in enumerate(nums):
            key=ha.twosum_put_int(x,target,i)
            if key!=-1:
                return [key,i]
        return
            
class hashtable:
    def __init__(self,n):
        self.length=2
        while(self.length<n):
            self.length=self.length*self.length
        self.li=[None]*self.length


    def put_int(self,obj):
        # h=id(obj)
        # print("h:",h)
        # hashval=h^(h>>16)
        print("self.length:",self.length)
        key=obj&(self.length-1)
        print("key:",key)
        if self.li[key] is None:
            self.li[key]=hashnode(obj)
        else:
            p=self.li[key]
            while(p.node is not None):
                if p.val==obj:#already exist,in some conditions,==need to be override
                    return
                p=p.node
            p.node=hashnode(obj)

    def twosum_put_int(self,obj,target,index):
        key=obj&(self.length-1)
        desire=target-obj
        desirekey=desire&(self.length-1)
        p=self.li[desirekey]

        while(p is not None):
            if p.val==desire:
                return p.key
            p=p.node
        #failed to hint,insert key
        if self.li[key] is None:
            self.li[key]=hashnode(obj)
            self.li[key].key=index
        else:
            p=self.li[key]
            while(p.node is not None):
                if p.val==desire:#already exist,in some conditions,==need to be override
                    return p.key#hint
                p=p.node
            p.node=hashnode(obj)
        return -1    

class hashnode:
    def __init__(self,val):
        self.key=-1
        self.val=val
        self.node=None

# if __name__=='__main__':
#     data=[2,7,11,15]
#     target=9
#     ts=Solution()
#     ts.twoSum(data,target)

