class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        result = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                result += 1

        else:
            for i in range(len(flowerbed)):
                # print(flowerbed, i, result)
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                        result += 1
                        flowerbed[i] = 1

                elif i == len(flowerbed) - 1:
                    if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                        result += 1

                else:
                    if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        result += 1
                        flowerbed[i] = 1

        return result >= n
