class Solution:
    """
    @param bits: a array represented by several bits.
    @return: whether the last character must be a one-bit character or not
    """
    def isOneBitCharacter(self, bits):
        index, n = 0, len(bits)
        if n == 1:
            return True
        if n == 2:
            return bits[0] == 1

        while index < n - 2:
            if bits[index] == 0:
                index += 1
            else:
                index += 2
        if index == n - 2 and bits[n - 2] == 1:
            return False
        else:
            return True
        # Write your code here
