#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
class Solution:
    def convertToTitle(self,n: int) -> str:
        l=[]
        n=n-1
        a=2
        b=1
        while(a>=0):
            # if(a==0 and b==25):
            #     break
            a=n//26-1
            b=n%26
            n=a
            l.append(b)
        length=len(l)
        l[0]=l[0]
        str=''
        l.reverse()
        for intx in l:
            str+=chr(intx+65)
        return str
if __name__=="__main__":
    t=Solution()
    print(t.convertToTitle(701))

