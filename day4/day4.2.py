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

        if word in ["MASMAS", "SAMMAS","SAMSAM","MASSAM"]:
            return True

        if len(word) > 6:
            return False

        if word in ["MAS", "SAM"]:
            # Move two to the left
            c_new = c - 2
            # Change direction to top-right
            dir = [-1, 1]
            return dfs(r, c_new, dir, word)

        # Continue in same direction
        return dfs(r + dir[0], c + dir[1], dir, word)

    result = 0

    for r in range(len(text)):
        for c in range(len(text[0])):
            if text[r][c] in ["M","S"]:
                # Set direction to bottom-right
                dir = [1, 1]
                if dfs(r, c, dir, ""):
                    result += 1

    return result

print(solution())
