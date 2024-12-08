def solution():
    # Read src.txt
    source = open("src.txt", "r")
    input = source.read().split("\n")
    source.close()

    def test_eval(test_val, nums):

        operator_combos = [""]
        for _ in range(len(nums) - 1):
            new_result = []
            for combo in operator_combos:
                new_result.append(combo + "*")
                new_result.append(combo + "+")
                new_result.append(combo + "c")
            operator_combos = new_result

        for combo in operator_combos:
            test_result = int(nums[0])

            for i in range(1, len(nums)):
                operator = combo[i - 1]
                if operator == "*":
                    test_result = int(test_result)
                    test_result *= int(nums[i])
                elif operator == "+":
                    test_result = int(test_result)
                    test_result += int(nums[i])
                elif operator == "c":
                    test_result = str(test_result)
                    test_result += str(nums[i])
            if int(test_result) == test_val:
                return True

        return False

    result = 0

    for test in input:

        colon_pos = test.index(":")
        test_val = int(test[:colon_pos])
        nums = test[colon_pos + 2 :].split(" ")

        if test_eval(test_val, nums):
            result += test_val

    return result


print(solution())
