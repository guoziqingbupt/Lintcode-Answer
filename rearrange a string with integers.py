class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """
    def rearrange(self, s):
        record = {}
        sumVal = 0
        result = ""
        for i in s:
            if i.isalpha():
                if i not in record:
                    record[i] = 1
                else:
                    record[i] += 1
            else:
                sumVal += int(i)

        for i in sorted(record):
            for j in range(record[i]):
                result += i
        if sumVal != 0:
            result += str(sumVal)
        return result
        # Write your code here
