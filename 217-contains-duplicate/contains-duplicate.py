class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        prevMap= set()

        for n in nums:
            if n in prevMap:
                return True
            
            prevMap.add(n)
        return False 
            