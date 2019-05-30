/*
 * @lc app=leetcode id=136 lang=java
 *
 * [136] Single Number
 */
class Solution {
    public int singleNumber(int[] nums) {
            for (int i =1; i < nums.length; i++) {
            nums[i] ^= nums[i-1];
        }
        return nums[nums.length-1];
    }
}

