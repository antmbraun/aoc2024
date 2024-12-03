# Read src.txt
source = open("src.txt", "r")
lines = source.read().split("\n")
source.close()

diff = 0
L = []
R = []

for line in lines:
  nums = line.split("   ")
  L.append(int(nums[0]))
  R.append(int(nums[1]))

L.sort()
R.sort()

for i in range(len(L)):
  diff = diff + abs(L[i] - R[i])

print(diff)

