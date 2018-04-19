"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param coordinates: The radars' coordinate
    @param radius: Detection radius of radars
    @return: The car was detected or not
    """
    def radarDetection(self, coordinates, radius):
        index = 0
        for point in coordinates:
            if point.x > 0 and min(abs(point.y - 1), abs(point.y)) < radius[index]:
                return "YES"
            elif abs(point.x) < radius[index]:
                if abs(point.y) < radius[index] or abs(point.y - 1) < radius[index]:
                    return "YES"
            index += 1
        return "NO"
        # Write your code here
