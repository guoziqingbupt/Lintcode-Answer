class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return a boolean, denote whether the array can be divided into k non-empty subsets whose sums are all equal
    """
    def partitiontoEqualSumSubsets(self, nums, k):
        sumNum = sum(nums)
        if sumNum % k != 0:
            return False
        nums.sort(reverse=True)
        target = sumNum // k
        visited = []

        index, n = 0, len(nums)
        while index < n:

            if index not in visited:

                if nums[index] == target:
                    index += 1
                    continue

                visited.append(index)
                begin = index + 1
                if not self.dfs(nums, target - nums[index], visited, begin):
                    return False
            index += 1
        return True

    def dfs(self, nums, target, visited, begin):
        if begin >= len(nums):
            return False
        if begin not in visited:

            if nums[begin] == target:
                visited.append(begin)
                return True
            elif nums[begin] > target:
                return self.dfs(nums, target, visited, begin + 1)
            else:
                visited.append(begin)
                if not self.dfs(nums, target - nums[begin], visited, begin + 1):
                    visited.pop()
                    return self.dfs(nums, target, visited, begin + 1)
                else:
                    return True
        else:
            return self.dfs(nums, target, visited, begin + 1)
        # write your code here

