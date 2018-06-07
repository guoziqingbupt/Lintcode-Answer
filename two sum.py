class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        hash_table = {}
        for i, ele in enumerate(numbers):
            hash_table[ele] = i

        for i, ele in enumerate(numbers):
            gap = target - ele
            if gap in hash_table.keys():
                return [i + 1, hash_table[gap] + 1]
                # write your code here
