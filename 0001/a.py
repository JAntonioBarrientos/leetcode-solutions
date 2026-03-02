class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = dict()

        ans = []
        for i in range(len(nums)):
            if nums[i] in complement:
                ans.append(i)
                ans.append(complement[nums[i]])
                return ans
                break

            complement[target-nums[i]] = i
        return []