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


        queue = [, down, left, right -> 0, 0 up, down, left, right -> 0, 1 ] 
        right -> recur call  -> append all neighbors onto stk

        temp = (1,1)
        '''

        initcolor = image[sr][sc]
        que = deque()
        que.append((sr, sc))

        def BFS(r, c):
            while que:
                temp = que.popleft()
                r, c = temp
                if r >= len(image) or r < 0 or c >= len(image[0]) or c < 0 or image[r][c] != initcolor or image[r][c] == color:
                    continue 
                
                if image[r][c] == initcolor:
                    image[r][c] = color

                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    que.append((r + dr, c + dc))
            return
            

        
        BFS(sr, sc)


        return image

            
