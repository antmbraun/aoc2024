from collections import defaultdict

def solution():
    # Read src.txt
    source = open("src.txt", "r")
    input = source.read().split("\n")
    source.close()

    result = set()

    # Find all the matching antennas
    antenna_types = defaultdict(list)

    for r, row in enumerate(input):
        for c, curr_char in enumerate(row):
            if curr_char != ".":
                antenna_types[curr_char].append((r, c))

    
    # Calculate the antinodes for each pair of antennas. Add to result if they are in bounds.
    for antennas in antenna_types.values():
        for i in range(len(antennas)):
            for j in range(i + 1, len(antennas)):
                # Antennas are automatically antinodes of themselves.
                antinode_one_r = antennas[i][0]
                antinode_one_c = antennas[i][1]
                antinode_two_r = antennas[j][0]
                antinode_two_c = antennas[j][1]
                
                diff = (antinode_one_r - antinode_two_r, antinode_one_c - antinode_two_c)
                
                while 0 <= antinode_one_r < len(input) and \
                   0 <= antinode_one_c < len(input[0]):
                   result.add((antinode_one_r, antinode_one_c))
                   antinode_one_r += diff[0]
                   antinode_one_c +=  diff[1] 

                while 0 <= antinode_two_r < len(input) and \
                   0 <= antinode_two_c < len(input[0]):
                    result.add((antinode_two_r, antinode_two_c))
                    antinode_two_r -= diff[0]
                    antinode_two_c -= diff[1] 

    return len(result)







print(solution())