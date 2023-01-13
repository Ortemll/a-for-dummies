def map_table(table):
    mapped_table = [[(None, 0) for j in range(WIDTH)] for i in range(HEIGHT)]  # 0 stands for "unmapped"
    mapped_table[0][0], mapped_table[-1][-1] = (-1, 1), (-1, 1)
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if mapped_table[j][i][1]: continue
            found_max = find_max((i, j), mapped_table)
            mapped_table[j][i] = (table[j][i] if found_max[0] is None else table[j][i]+found_max[0], 1)
    return mapped_table


def find_max(pos, mapped_table):
    col, row = pos  # all the "lower" cells expected to be already mapped
    max_num, max_pos = None, (None, None)
    if row == 0:
        max_num, max_pos = mapped_table[row][col-1], (col-1, row)
    elif col == 0:
        max_num, max_pos = mapped_table[row-1][col], (col, row-1)
    else:
        if int(mapped_table[row][col-1], 2) > int(mapped_table[row-1][col], 2):
            max_num, max_pos = mapped_table[row][col-1], (col-1, row)
        else:
            max_num, max_pos = mapped_table[row-1][col], (col, row-1)
    return max_num, max_pos



def main():
    from pprint import pprint
    global WIDTH, HEIGHT, JUMPS_COUNT
    xlfile = open('/home/student/Загрузки/18-147.csv', 'rt', encoding='utf8')
    table = [line.strip().split(',') for line in xlfile if line]
    WIDTH, HEIGHT = len(table[0]), len(table)
    pprint(table)
    mapped_table = map_table(table)
    pprint(mapped_table)

    pos = (0, 0)
    summ = table[0][0]
    while pos != (WIDTH-1, HEIGHT-1):
        _, goto = find_max(pos, mapped_table)
        if goto == (None, None):
            summ += table[-1][-1]
            pos = (WIDTH-1, HEIGHT-1)
            break
        add = table[goto[1]][goto[0]]
        summ += add
        pos = goto
    print(summ)


if __name__ == "__main__":
    main()
