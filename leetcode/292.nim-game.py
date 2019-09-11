#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#
import leetcode.minimax
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n<4:
            return True
        return False
     
