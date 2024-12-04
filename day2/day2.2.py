def solution():
    # Read src.txt
    source = open("src.txt", "r")
    lines = source.read().split("\n")
    source.close()

    result = 0

    for line in lines:
        report = line.split(" ")
        if isReportSafe(report):
            result += 1

    return result

def isReportSafe(report, is_damper_check = False):
    prev_diff = 0
    flagReport = False

    for i in range(1, len(report)):
        curr_diff = int(report[i]) - int(report[i - 1])

        # Check that difference is within range
        if not 1 <= abs(curr_diff) <= 3:
            flagReport = True

        # Check for change in direction
        if curr_diff * prev_diff < 0:
            flagReport = True

        if flagReport:
          if not is_damper_check:
              return isReportSafe(report[:i] + report[i+1:], True) or isReportSafe(report[:i-1] + report[i:], True) or isReportSafe(report[:i-2] + report[i-1:], True) 
          else:
              return False
          
        prev_diff = curr_diff

    return True

print(solution())