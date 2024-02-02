class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        quadX = [sc + 1, sc - 1]
        quadY = [sr + 1, sr - 1]

        image[sc][sr] = color

        for x in quadX:
            if x >= 0 and x < len(image) and image[sr][x]:
                image = self.floodFill(image, sr, x, color)

        for y in quadY:
            if y >= 0 and y < len(image[0]):
                image = self.floodFill(image, y, sc, color)

        return image
