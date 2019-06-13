#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
''' version 1 该版本的最大优点是立即返回
from typing import List
class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        print()
        self.maxX=len(board[0])
        self.maxY=len(board)
        self.visit=[[0 for i in range(self.maxX)] for j in range(self.maxY)]
        for y in range(self.maxY):
            for x in range(self.maxX): 
                # self.visit=[[0 for i in range(self.maxX)] for j in range(self.maxY)]
                if(self.backtrace(board,word,x,y,n=0)):
                    print("hit")
                    return True
        return False

    def backtrace(self, board: List[List[str]], word: str,x,y,n)->bool:
        lb=False
        rb=False
        ub=False
        db=False
        if(self.visit[y][x]==1):
            return False
        else:
            self.visit[y][x]=1
        if(board[y][x]==word[n]):
            # print(y,x,board[y][x])
            # for line in self.visit:
            #     print(line)
            if(n==len(word)-1):
                return True
            if((x-1)>=0):
                lb=self.backtrace(board,word,x-1,y,n+1)
                # self.visit[y][x-1]=0
                if(lb):
                    return True
            if((x+1)<self.maxX):
                rb=self.backtrace(board,word,x+1,y,n+1)
                # self.visit[y][x+1]=0
                if(rb):
                    return True
            if((y-1)>=0):
                db=self.backtrace(board,word,x,y-1,n+1)
                # self.visit[y-1][x]=0
                if(db):
                    return True
            if((y+1)<self.maxY):
                ub=self.backtrace(board,word,x,y+1,n+1)
                # self.visit[y+1][x]=0
                if(ub):
                    return True
            # return lb or rb or ub or db
        self.visit[y][x]=0
        return False
'''
from typing import List
class Solution:
    
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res


if __name__=='__main__':
    l=[["a","b","c","d"]]
    s=Solution()
    s.exist(l,"bc")
    s.backtrace


