"""
ID: tnguye28
LANG: PYTHON2
TASK: crypt1
"""
fin = open('crypt1.in', 'r')
temp = fin.readlines()
N = int(temp[0].strip())
digits = temp[1].strip().split(' ')
digits = [int(_) for _ in digits]
fin.close()

result = 0

def legit_num(x):
    while x:
        r = x % 10
        x = x // 10
        if r not in digits:
            return False

    return True

for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                for e in digits:
                    abc = a * 100 + b * 10 + c
                    p1 = abc * e
                    p2 = abc * d

                    if p1 <= 999 and p2 <= 999 and 1000 <= p1 + p2 * 10 <= 9999 and legit_num(p1) and legit_num(p2) and legit_num(p2 * 10 + p1):
                        result += 1



with open('crypt1.out', 'w') as fout:
    fout.write(str(result) + '\n')