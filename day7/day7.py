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
            operator_combos = new_result

        for combo in operator_combos:
            test_result = nums[0]
            for i in range(1, len(nums)):
                if combo[i - 1] == "*":
                    test_result *= nums[i]
                elif combo[i - 1] == "+":
                    test_result += nums[i]
            if test_result == test_val:
                return True

        return False

    result = 0

    for test in input:

        colon_pos = test.index(":")
        test_val = int(test[:colon_pos])
        nums = test[colon_pos + 2 :].split(" ")
        nums = [int(num) for num in nums]

        if test_eval(test_val, nums):
            result += test_val

    return result


print(solution())
