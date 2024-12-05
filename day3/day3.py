def solution():
    # Read src.txt
    source = open("src.txt", "r")
    text = source.read()
    source.close()

    result = 0

    L = 0
    start_find_nums = False
    num_string = ""

    for R in range(3, len(text) - 1):
        if start_find_nums:
          if text[R] != ")":
            num_string += text[R]

        if text[L:R+1] == "mul(":
            start_find_nums = True

        if not start_find_nums:
          L += 1

    # print(text)

solution()
