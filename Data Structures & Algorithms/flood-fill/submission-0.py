class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        horizontally or vertically 

        sr , sc starting point. color is what we want to change 


        [0,1,0],
        [1,0,0], sr = 0, sc = 0, color = 0

        if image[r][c] == initcolor:
            image[r][c] = color

        DFS(r, c)
        base case
        if image[r][c] == initcolor:
            image[r][c] = color

        boundary check / exit check
        if r > len(image) or r < 0 or c > image[0] or c < 0 or image[r][c] != initcolor:
            return 

        up, left ,right, down
        DFS()

        
        '''

        initcolor = image[sr][sc]

        def DFS(r, c):
            if r >= len(image) or r < 0 or c >= len(image[0]) or c < 0 or image[r][c] != initcolor or image[r][c] == color:
                return 
            
            if image[r][c] == initcolor:
                image[r][c] = color

            DFS(r + 1, c)
            DFS(r - 1, c)
            DFS(r, c + 1)
            DFS(r, c - 1)

        
        DFS(sr, sc)
        return image

            
