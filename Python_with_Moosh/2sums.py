# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
nums=[3,4,5,3,2,7]
target=7
reminder=0
reminder2=0       
for i in nums:
    reminder=target-i
    reminder2=nums.index(reminder)