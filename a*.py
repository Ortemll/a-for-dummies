def right():
    pos[0] += 1
def down():
    pos[1] += 1
def jump(x, y):  # нет проверки неотрицательности x, y
    global JUMPS_COUNT
    pos[0], pos[1] = pos[0] + x, pos[1] + y
    JUMPS_COUNT = 0


# def search_for_closest(pos):
#     col, row = pos
#     return [(x, row) for x in range(col, WIDTH) if table[x][row]>0] +\
#         [(col, y) for y in range(row, HEIGHT) if table[col][y]>0]  # нет обработки нулей
def map_table(table):  # freaking A* algorithm
    mapped_table = [[(None, 0) for j in range(WIDTH)] for i in range(HEIGHT)]  # 0 stands for "unmapped"
    mapped_table[0][0], mapped_table[-1][-1] = (-1, 1), (-1, 1)
    # mapping negative numbers
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if mapped_table[i][j][1]: continue
            if table[i][j] <= 0:
                mapped_table[i][j] = (0, 1)
    for j in range(HEIGHT-1, -1, -1):
        for i in range(WIDTH-1, -1, -1):
            if mapped_table[i][j][1]: continue
            max_pos = find_max_pos((i, j))

def find_max_pos(pos, mapped_table):
    col, row = pos  # all the "lower" cells expected to be already mapped
    max_pos, max_num = (None, None), None
    for j in range(col, HEIGHT):
        for i in range(row, WIDTH):
            if mapped_table[i][j][0] > 0 and mapped_table[i][j][0] > max_num:
                max_num, max_pos = mapped_table[i][j][0], (i, j)
                break
    return max_pos


xlfile = open('/home/student/Загрузки/18-143.csv', 'rt', encoding='utf8')
table = [list(map(int, line.split(',')[1:-1])) for line in xlfile if line][1:]
WIDTH, HEIGHT = len(table[0]), len(table)
JUMPS_COUNT = 0
print(table)

pos = (0, 0)
summ = table[0][0] + table[-1][-1]
for

