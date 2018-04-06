class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        if len(array) == 0:
            return []
        result = [array[0]]

        for record in array[1:]:

            index = len(result) - 1

            while index >= 0 and result[index][1] < record[1]:
                index -= 1

            while index >= 0 and result[index][1] == record[1] and result[index][0] > record[0]:
                index -= 1

            result.insert(index + 1, record)
        return result
        # Write your code here

