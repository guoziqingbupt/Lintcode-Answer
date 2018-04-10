"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x.start)
        index, n = 0, len(intervals)

        while index + 1 < n:
            if intervals[index + 1].start < intervals[index].end:
                return False
            index += 1
        return True
        # Write your code here