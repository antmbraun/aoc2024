def solution():
    # Read src.txt
    source = open("src.txt", "r")
    input = source.read()
    source.close()


    # Create a dictionary of ids to their qty of blocks and proceeding free space.
    files_dict = {}

    id = 0
    for i, n in enumerate(input):
        if i % 2 == 0:
            files_dict[id] = {
                'blocks': int(n),
            }
            if i < len(input) - 1:
                files_dict[id]['free'] = int(input[i + 1])
            id += 1


    # Create the result string by taking blocks from the right and inserting them from the left.
    sumstring = ""
    i = 0 
    j = len(files_dict) - 1

    while i < j:
        i_block = files_dict[i]
        j_block = files_dict[j]

        sumstring += str(i) * i_block['blocks']
        
        while i_block['free'] > 0 and j_block['blocks'] > 0:
            sumstring += str(j)
            i_block['free'] -= 1
            j_block['blocks'] -= 1
            if j_block['blocks'] == 0:
                j -= 1
                j_block = files_dict[j]
        
        i += 1

    # Add the remaining blocks
    sumstring += str(j) * files_dict[j]['blocks'] 
    
    checksum = 0
    for i, n in enumerate(sumstring):
        checksum += i * int(n)

    return checksum
            
print(solution())