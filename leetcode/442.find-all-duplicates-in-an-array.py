#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
from typing import List
class Solution:
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        length=len(nums)
        l=[None]*length
        for n in nums:
            hash=n%length
            if l[hash]==n:
                res.append(n)
            else:
                l[hash]=n
        return res

if __name__=='__main__':
    sol=Solution()
    l=[4,3,2,7,8,2,3,1]
    res=sol.findDuplicates(l)
    print(res)
'''
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        length=len(nums)
        l=[None]*length
        for n in nums:
            hash=abs(n)%length
            if nums[hash]<0:
                res.append(abs(n))
            else:
                nums[hash]=-nums[hash]
        return res
if __name__=='__main__':
    sol=Solution()
    l=[4,3,2,7,8,2,3,1]
    res=sol.findDuplicates(l)
    print(res)        
