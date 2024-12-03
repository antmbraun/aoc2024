def solution():
    # Read src.txt
    source = open("src.txt", "r")
    lines = source.read().split("\n")
    source.close()

    result = 0

    for line in lines:
        level = line.split(" ")
        if isLevelSafe(level):
            result += 1

    return result

def isLevelSafe(level):
    prev_diff = 0

    for i in range(1, len(level)):
        curr_diff = int(level[i]) - int(level[i - 1])

        # Check that difference is within range
        if not 1 <= abs(curr_diff) <= 3:
            return False

        # Check for change in direction
        if curr_diff * prev_diff < 0:
            return False

        prev_diff = curr_diff

    return True

print(solution())