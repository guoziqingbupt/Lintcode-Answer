"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):

        n1, n2 = len(list1), len(list2)
        if n1 == 0:
            return list2
        elif n2 == 0:
            return list1

        if list1[0].start < list2[0].start:
            result = [list1[0]]
        else:
            result = [list2[0]]

        index1, index2 = 0, 0
        while index1 < n1 and index2 < n2:
            if list1[index1].start <= list2[index2].start:
                cur = self.helper(result[-1], list1[index1])
                if cur:
                    result[-1] = cur
                    index1 += 1
                else:
                    result.append(list1[index1])
                continue

            if list2[index2].start < list1[index1].start:
                cur = self.helper(result[-1], list2[index2])
                if cur:
                    result[-1] = cur
                    index2 += 1
                else:
                    result.append(list2[index2])
                continue

        while index1 < n1:
            cur = self.helper(result[-1], list1[index1])
            if not cur:
                break
            result[-1] = cur
            index1 += 1
        result += list1[index1:]

        while index2 < n2:
            cur = self.helper(result[-1], list2[index2])
            if not cur:
                break
            result[-1] = cur
            index2 += 1
        result += list2[index2:]
        return result

    def helper(self, interval1, interval2):
        if interval1.start <= interval2.start <= interval1.end:
            return Interval(interval1.start, max(interval1.end, interval2.end))
        elif interval1.start <= interval2.end <= interval1.end:
            return Interval(min(interval1.start, interval2.start), interval1.end)
        # write your code here