class Solution:
    """
    @param ages: The ages
    @return: The answer
    """
    def friendRequest(self, ages):
        count = 0
        index, n = 0, len(ages)

        while index < n:
            cur = ages[index]
            for i in ages[:index] + ages[index + 1:]:
                if i <= 0.5 * cur + 7 or i > cur or (i < 100 and cur > 100):
                    continue
                else:
                    count += 1
            index += 1
        return count
        # Write your code here