#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
class MedianFinder:

    def __init__(self):
        self.li=[None]
        """
        initialize your data structure here.
        """

    def addNum(self, num: int) -> None:
        self.li[0]=num
        self.li.append(num)
        for i in range(len(self.li)-2,-1,-1):
            if self.li[0]<self.li[i]:
                self.li[i+1]=self.li[i]
            else:
                self.li[i+1]=self.li[0]
                break

    def findMedian(self) -> float:
        if len(self.li)==1:
            return
        else:
            length=len(self.li)-1
            if length%2==0:
                return  float((self.li[length//2]+self.li[length//2+1])/2)
            else:
                return  float(self.li[length//2+1])

if __name__=='__main__':
    s=MedianFinder()
    l=s.li
    s.addNum(-1)
    s.addNum(-2)
    an=s.findMedian()
    s.addNum(2)
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

