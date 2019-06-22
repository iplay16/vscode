#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict={}
        
        for word in strs:
            word_sort=str(sorted(word))
            if word_sort in word_dict:
                word_dict[word_sort].append(word)
            else:
                word_dict[word_sort]=[word]
        
        return list(word_dict.values())       

