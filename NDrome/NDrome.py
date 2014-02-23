import sys

def isEqual(m,n):
  length = len(n)
  
  for i in range(0, length):
    if m[i] != n[i]:
      return False
      
  return True
  
def isPali(n):
  return n == n[::-1]

##str = raw_input("String: ")##sys.stdin.read(1)

inputs = ["ab|1",
"123456123455|6",
"123456789987654321|9",
"1234abcd|4",
"123456789123456789|9",
"123456789|9",
"12341234|4",
"123456781234|4",
"ab ba|1",
"abcdedcba|1",
"abcddcba|1",
"121212|2",
"123456789789456123|3",
"123456789456123|3",
"123456|6",
"123456123456|6",
"abcdef123456abcdef|6"]

for str in inputs:
  length = len(str)

  n = 0

  for i in range(0,length):
    if str[i] == "|":
      s = str[:i]
      for j in range(i+1,length):
        n = n*10 + int(str[j])
      
  length = len(s)

  if length < n:
    "%s|0" % str
  
  divided = []


  if n != 1 and n != length:
    for i in range(0, length, n):
      divided.append(s[i:i+n])

  else:
    if isPali(s):
      print "%s|1" % str
    else:
      print "%s|0" % str  
    continue
  
  flag = False
  length = len(divided)
  for i in range(0, length/2):
    if isEqual(divided[i], divided[length - 1 - i]) != True:
      print "%s|0" % str
      flag = True
      
  if flag == True:
    continue
    
  print "%s|1" % str