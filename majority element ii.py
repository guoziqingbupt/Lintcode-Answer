class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        hashTable = {}

        for i in nums:
            if len(hashTable) < 3:
                if i in hashTable:
                    hashTable[i] += 1
                else:
                    hashTable[i] = 1
            else:
                temp = []
                for ele in hashTable:
                    hashTable[ele] -= 1
                    if hashTable[ele] == 0:
                        temp.append(ele)
                for ele in temp:
                    hashTable.pop(ele)

        for ele in hashTable:
            hashTable[ele] = 0

        for i in nums:
            if i in hashTable:
                hashTable[i] += 1
        return max(hashTable, key=lambda x: hashTable[x])
        # write your code here

obj = Solution()
print(obj.majorityNumber([7,1,7,7,61,61,61,10,10,10,61]))