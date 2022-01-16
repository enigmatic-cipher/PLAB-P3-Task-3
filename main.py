"""
Given n as input. Print following pattern using For loop.
n = 5
Expected Output:
#10#15#20#25#30
"""

n = 5
pt = "#"
st = ""
for i in range(2,n+2):
  st = pt + str(n*i)
  print(st, end="")
  
