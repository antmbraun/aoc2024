import copy


def solution():
    # Read src.txt
    source = open("src.txt", "r")
    input = source.read().split("\n")
    source.close()

    result = 0

    # Find the starting position
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "^":
                start_pos = (r, c)

    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == ".": 
                test_input = copy.deepcopy(input)
                test_input[r] = test_input[r][:c] + "#" + test_input[r][c + 1:]
                if isStuckinLoop(test_input, start_pos):
                    result += 1
    return result


def isStuckinLoop(test_input, start_pos):

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    tracks = set()

    # Initialize direction to North
    dir_idx = 0

    r_curr = start_pos[0]
    c_curr = start_pos[1]

    while True:
        r_next = r_curr + directions[dir_idx][0]
        c_next = c_curr + directions[dir_idx][1]

        # Out of bounds check. If the next step is out of bounds, we've escaped.
        if r_next < 0 or r_next >= len(test_input) or c_next < 0 or c_next >= len(test_input[0]):
            return False

        # Wall check: Change direction
        if test_input[r_next][c_next] == "#":
            dir_idx = (dir_idx + 1) % 4
            continue

        # Take a step forward
        r_curr = r_next
        c_curr = c_next

        # Remember this step. If we've done it before, we are in a loop.
        track = (r_curr, c_curr, directions[dir_idx][0], directions[dir_idx][1])
        if track in tracks:
            return True
        else:
            tracks.add(track)


print(solution())
