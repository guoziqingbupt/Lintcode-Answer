class Solution:
    """
    @param target: the destination
    @return: the minimum number of steps
    """
    def reachNumber(self, target):
        step, count = 0, 0
        while count < abs(target):
            step += 1
            count += step

        gap = count - target
        if gap % 2 == 0:
            return step
        elif (gap + (step + 1)) % 2 == 0:
            return step + 1
        else:
            return step + 2
        # Write your code here

