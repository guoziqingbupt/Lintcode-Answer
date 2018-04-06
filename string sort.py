class Solution:
    """
    @param str: the string that needs to be sorted
    @return: sorted string
    """
    def stringSort(self, str):

        # key: value = char: count
        record = {}
        for i in str:
            if i not in record:
                record[i] = 1
            else:
                record[i] += 1

        # sort the dictionary and put the key into the temp list
        temp = []
        for i in sorted(record, key=lambda x: record[x], reverse=True):
            temp.append(i)

        result = ""
        curCount = record[temp[0]]
        begin, cur = 0, 0
        n = len(temp)
        while cur < n:
            while cur < n and record[temp[cur]] == curCount:
                cur += 1
            for i in sorted(temp[begin: cur]):
                result += i * record[i]
            begin = cur
            if cur < n:
                curCount = record[temp[cur]]
        return result
        # Write your code here
