class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        - int array nums
        - return true if any values appears at least twice and false if every element is distinct

        - we can use hashmap/dictionary for this 
        """

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False