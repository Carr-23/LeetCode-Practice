class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        quadX = [sc + 1, sc - 1]
        quadY = [sr + 1, sr - 1]
        cur = image[sr][sc]

        image[sr][sc] = color

        for x in quadX:
            if (
                x >= 0
                and x < len(image[0])
                and image[sr][x] == cur
                and image[sr][x] != color
            ):
                image = self.floodFill(image, sr, x, color)

        for y in quadY:
            if (
                y >= 0
                and y < len(image)
                and image[y][sc] == cur
                and image[y][sc] != color
            ):
                image = self.floodFill(image, y, sc, color)

        return image
