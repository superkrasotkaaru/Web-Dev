# Power - Mod Power
# Sample Input

# 3
# 4
# 5
# Sample Output

# 81
# 1
import math
a = int(input())
b = int(input())
m = int(input())
c = math.pow(a, b)
d = c%m
print(int(c))
print(int(d))