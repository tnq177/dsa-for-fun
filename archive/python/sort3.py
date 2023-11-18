"""
ID: tnguye28
LANG: PYTHON2
TASK: sort3
"""
fin = open('sort3.in', 'r')
temp = fin.readlines()
fin.close()

N = int(temp[0].strip())
num1 = num2 = num3 = 0
nums = []
for i in xrange(N):
    num = int(temp[i+1])
    if num == 1:
        num1 += 1
    elif num == 2:
        num2 += 1
    elif num == 3:
        num3 += 1

    nums.append(num)

result = 0
for i in xrange(num1):
    for j in xrange(num1, num1+num2):
        if nums[i] == 2 and nums[j] == 1:
            nums[i] = 1
            nums[j] = 2
            result += 1
for i in xrange(num1):
    for j in xrange(num1+num2, num1+num2+num3):
        if nums[i] == 3 and nums[j] == 1:
            nums[i] = 1
            nums[j] = 3
            result += 1
for i in xrange(num1, num1+num2):
    for j in xrange(num1+num2, num1+num2+num3):
        if nums[i] == 3 and nums[j] == 2:
            nums[i] = 2
            nums[j] = 3
            result += 1
for i in xrange(num1):
    if nums[i] != 1:
        result += 2

with open('sort3.out', 'w') as fout:
    fout.write(str(result) + '\n')