def solution():
    # Read src.txt
    source = open("src.txt", "r")
    input = source.read().split("\n")
    source.close()

    visited = set()

    # Find the starting position

    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "^":
                start_pos = (r, c)
    
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    dir_idx = 0

    visited.add((start_pos[0], start_pos[1]))

    r_curr = start_pos[0] + directions[dir_idx][0]
    c_curr = start_pos[1] + directions[dir_idx][1]

    while True:
        
        visited.add((r_curr, c_curr))

        r_next = r_curr + directions[dir_idx][0]
        c_next = c_curr + directions[dir_idx][1]

        # Out of bounds check
        if not (0 <= r_next < len(input) and 0 <= c_next < len(input[0])):
            break
          
        # Wall check
        if input[r_next][c_next] == "#":
          dir_idx = (dir_idx + 1) % 4

        r_curr = r_curr + directions[dir_idx][0]
        c_curr = c_curr + directions[dir_idx][1]

    return len(visited)

print(solution())
            
