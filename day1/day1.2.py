# Read src.txt
source = open("src.txt", "r")
lines = source.read().split("\n")
source.close()

Lnums = set()
Rcounts = {}

for line in lines:
  nums = line.split("   ")
  Lnum = int(nums[0])
  Rnum = int(nums[1])

  Lnums.add(Lnum)
  
  if Rnum in Rcounts:
    Rcounts[Rnum] = Rcounts[Rnum] + 1 
  else:
    Rcounts[Rnum] = 1

similarity = 0

for num in Lnums:
  if num in Rcounts:
    similarity += num * Rcounts[num]

print(similarity)
