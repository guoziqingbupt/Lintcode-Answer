class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    def canPlaceFlowers(self, flowerbed, n):
        index, size = 0, len(flowerbed)

        if size == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n <= 0

        count = 0
        while index < size:
            if index == 0:
                if flowerbed[index + 1] == 0 and flowerbed[index] == 0:
                    count += 1
                    flowerbed[index] = 1
                    n -= 1
            elif index == size - 1:
                if flowerbed[index - 1] == 0 and flowerbed[index] == 0:
                    count += 1
                    flowerbed[index] = 1
            else:
                if flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0 and flowerbed[index] == 0:
                    flowerbed[index] = 1
                    count += 1
            index += 1
        return n <= count
        # Write your code here