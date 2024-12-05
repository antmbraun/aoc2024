def solution():
    # Read src.txt
    source = open("src.txt", "r")
    text = source.read().split("\n")
    source.close()

    def dfs(r, c, dir, word):
        # Out of bounds check
        if r < 0 or r >= len(text) or c < 0 or c >= len(text[0]):
            return False
        
        word += text[r][c]

        # "XMAS" check
        if word == "XMAS":
          return True

        if word not in ["X", "XM", "XMA"]:
            return False 
         
        if len(word) > 4:
            return False
        
        # Continue in same direction
        return dfs(r + dir[0], c + dir[1], dir, word)

    result = 0

    directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
        [-1, -1],
        [1, 1],
        [-1, 1],
        [1, -1]
    ]

    for r in range(len(text)):
        for c in range(len(text[0])):
            if text[r][c] == "X":
                for dir in directions:
                  if dfs(r, c, dir, ""):
                      result += 1
  
    return result


print(solution())