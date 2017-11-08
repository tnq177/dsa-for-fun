"""
ID: tnguye28
LANG: PYTHON2
TASK: castle
"""
from collections import deque

fin = open('castle.in', 'r')
temp = fin.readlines()
fin.close()

ncols, nrows = temp[0].strip().split(' ')
ncols, nrows = int(ncols), int(nrows)
walls = []
for i in xrange(nrows):
    row = temp[i+1].strip().split(' ')
    row = [int(x) for x in row]
    walls.append(row)

rooms = [[0] * ncols for _ in xrange(nrows)]
room_count = 0

def mark_room(room_row, room_col):
    stack = [(room_row, room_col)]
    while stack:
        r, c = stack.pop()
        rooms[r][c] = room_count
        
        wall_value = walls[r][c]
        W, N, E, S = wall_value & 1, wall_value & 2, wall_value & 4, wall_value & 8

        if not W and 0 <= c-1 < ncols and not rooms[r][c-1]:
            stack.append((r, c-1))

        if not N and 0 <= r-1 < nrows and not rooms[r-1][c]:
            stack.append((r-1, c))

        if not E and 0 <= c+1 < ncols and not rooms[r][c+1]:
            stack.append((r, c+1))

        if not S and 0 <= r+1 < nrows and not rooms[r+1][c]:
            stack.append((r+1, c))

for r in xrange(nrows):
    for c in xrange(ncols):
        if not rooms[r][c]:
            room_count += 1
            mark_room(r, c)

room_sizes = [0] * room_count
for r in xrange(nrows):
    for c in xrange(ncols):
        room_sizes[rooms[r][c]-1] += 1
max_room_size = max(room_sizes)

def can_break(has_wall, direction, r, c, dr, dc, values):
    if has_wall and 0 <= r+dr < nrows and 0 <= c+dc < ncols and rooms[r+dr][c+dc] != rooms[r][c]:
        temp = room_sizes[rooms[r+dr][c+dc]-1] + room_sizes[rooms[r][c]-1]
        if temp > values[0]:
            values[0] = temp
            values[1] = r
            values[2] = c
            values[3] = direction


values = [0, 0, 0, None]
for c in xrange(ncols):
    for r in xrange(nrows-1, -1, -1):
        wall_value = walls[r][c]
        W, N, E, S = wall_value & 1, wall_value & 2, wall_value & 4, wall_value & 8

        can_break(N, 'N', r, c, -1, 0, values)
        can_break(E, 'E', r, c, 0, +1, values)
        can_break(S, 'S', r, c, 1, 0, values)
        can_break(W, 'W', r, c, 0, -1, values)

with open('castle.out', 'w') as fout:
    fout.write(str(room_count) + '\n')
    fout.write(str(max_room_size) + '\n')
    fout.write(str(values[0]) + '\n')
    fout.write('{} {} {}\n'.format(values[1]+1, values[2]+1, values[3]))
