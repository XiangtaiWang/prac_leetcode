class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = dict()
        for index, num in enumerate(nums):
            if hashmap.get(num) is None:
                hashmap[num] = [index]
            else:
                hashmap[num].append(index)

        for index, num in enumerate(nums):
            dif = target - num
            if hashmap.get(dif) is not None:
                matched_index = next((dif_index for dif_index in hashmap.get(dif) if dif_index!=index), None)
                if matched_index is None:
                    continue

                result = [index, matched_index]
                result.sort()
                return result
    

s = Solution()
nums = [3,4,5,6]
target = 7
r = s.twoSum(nums=nums, target=target)
assert r == [0,1]

nums = [4,5,6]
target = 10
r = s.twoSum(nums=nums, target=target)
assert r == [0,2]

nums = [5,5]
target = 10
r = s.twoSum(nums=nums, target=target)
assert r == [0,1]

nums=[1,3,4,2]
target=6
r = s.twoSum(nums=nums, target=target)
assert r == [2,3]
print("all pass")