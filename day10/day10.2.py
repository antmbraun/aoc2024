def solution():
    # Read src.txt
    source = open("src.txt", "r")
    input = source.read().split('\n')
    source.close()
    
    directions = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
    ]

    def dfs(r, c):
        if input[r][c] == '9':
            return 1
        
        count = 0

        for dir in directions:
            r_new = r + dir[0]
            c_new = c + dir[1]
            if (
              r_new < len(input) and
              r_new >= 0 and
              c_new < len(input[0]) and
              c_new >= 0 and
              int(input[r_new][c_new]) - int(input[r][c]) == 1):
                  count += dfs(r_new, c_new)
        return count
    
    result = 0
    for r, row in enumerate(input):
        for c, num in enumerate(row):
            if num == '0':
                result += dfs(r, c)

    return result


print(solution())