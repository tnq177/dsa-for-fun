"""
ID: toannq12
LANG: PYTHON3
TASK: test
"""

def main():
    fin = open ('test.in', 'r')
    fout = open ('test.out', 'w')
    x,y = map(int, fin.readline().split())
    sum = x+y
    fout.write (str(sum) + '\n')
    fout.close()


if __name__ == "__main__":
    main()