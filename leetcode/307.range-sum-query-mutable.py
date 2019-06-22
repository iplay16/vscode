#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
import time
import sys
from typing import List
class Node:
    def __init__(self):
        self.l=0
        self.r=0
        self.sum=0

class NumArray:
    def __init__(self, nums: List[int]):
        start=time.clock()
        print("function",sys._getframe().f_code.co_name)
        if not nums:
            return
        self.sum=0
        self.nums=nums
        # print("nums is :",self.nums)
        lengthofn=len(self.nums)*3+1
        self.n=[None for i in range(lengthofn)]
        self.build(0,len(self.nums)-1,0)
        elapsed = (time.clock() - start)
        print("Time used:",elapsed)

    def update(self, i: int, val: int) -> None:
        start=time.clock()
        print("function update")
        # print("updata:",i,"val",val)
        self.add(i,val-self.nums[i],0)
        self.nums[i]=val
        # for x in self.n:
        #     if x:
        #         print(x.sum,"l:",x.l,"r:",x.r)
        elapsed = (time.clock() - start)
        print("Time used:",elapsed)

    def sumRange(self, i: int, j: int) -> int:
        start=time.clock()
        print("function update")
        self.sum=0
        self.query(i,j,0) #update sum
        # print("sum:",self.sum)
        elapsed = (time.clock() - start)
        print("Time used:",elapsed)
        return self.sum
    
    def build(self,l,r,idx):
        self.n[idx] = Node()
        self.n[idx].l = l
        self.n[idx].r = r
        if l == r:
            self.n[idx].sum = self.nums[l]
        else:
            self.build(l, (l + r) >> 1, (idx << 1) + 1)
            self.build(((l + r) >> 1) + 1, r, (idx << 1) + 2)
            self.n[idx].sum = self.n[(idx << 1) + 1].sum + self.n[(idx << 1) + 2].sum
    
    def add(self,i,j,idx): #第i个营地增加j个人
        #从根节点不断往下更改，只要包含点i的线段都增加数量j
        self.n[idx].sum += j
        if self.n[idx].l == i and self.n[idx].r == i: #如果找到i的叶子节点则停止
            return
        if i <= ((self.n[idx].l + self.n[idx].r) >> 1): # 如果i在线段左边
            self.add(i, j, (idx << 1) + 1) # 递归进入左子节点
        else: # 如果i在线段右边
            self.add(i, j, (idx << 1) + 2) # 递归进入右子节点

    def query(self,l,r, idx):#初始idx为0，即从根节点开始查找
        if (l <= self.n[idx].l and r >= self.n[idx].r):
            self.sum += self.n[idx].sum
        else :
            mid = (self.n[idx].l + self.n[idx].r) >> 1
            if (r <= mid): #要查询的区间在左边
                self.query(l, r, (idx << 1) + 1)
            elif (l > mid): # 要查询的区间在右边
                self.query(l, r, (idx << 1) + 2)
            else: #要查询的区间在中间，分段查询，左右都查
                self.query(l, r, (idx << 1) + 1)
                self.query(l, r, (idx << 1) + 2) 

# '''
import tools
if __name__=='__main__':
    action=["NumArray","update","update","update","sumRange","update","sumRange","update","sumRange","sumRange","update"]
    data=[[[7,2,7,2,0]],[4,6],[0,2],[0,9],[4,4],[3,8],[0,4],[4,1],[0,3],[0,4],[0,4]]
    # expected_answer: [null,null,null,null,6,null,32,null,26,27,null]
    # action= ["NumArray","sumRange","update","sumRange"]
    # data=[[[1,3,5]],[0,2],[1,2],[0,2]]
    li=tools.runTest(NumArray(data[0][0]),action,data)
    # print(li)
# '''
