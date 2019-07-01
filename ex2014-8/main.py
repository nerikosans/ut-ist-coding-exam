import numpy as np
import scipy as sp
import math
# 16:46
# 18:09

# (1)
def f_1():
    f = open('program.c', encoding='utf-8')
    program = f.read()
    print ('# of ; = ' + str(program.count(';')))

# (2)
def f_2():
    f = open('program.c', encoding='utf-8')
    i = 0
    for line in f.readlines():
        i+=1
        print(str(i) + ': \t' + line.replace('\n', ''))

# (3)
def f_3():
    f = open('program.c', encoding='utf-8')
    line_prev = None
    for line in f.readlines():
        line = line.replace('\n', '')
        if (line_prev == line):
            print(line)
        line_prev = line

# (4)
def f_4():
    f = open('program.c', encoding='utf-8')
    history = []
    dup_line_count = 0
    for line in f.readlines():
        line = line.replace('\n', '')
        if (line in history):
            dup_line_count+=1
            print(line)
        history.append(line)
    print(dup_line_count)

# f_4()

# (5)
def zip_line(line1, line2):
    len1, len2 = len(line1), len(line2)
    if (len1 < len2):
        line1 += ''.join([' ' for _ in range(len2-len1)])
    elif (len1 < len2):
        line2 += ''.join([' ' for _ in range(len1-len2)])
    return list(zip(line1, line2))

def is_similar_pair(line1, line2):
    ziped = zip_line(line1, line2)
    diff_count = sum([
        1 if p != q else 0
        for (p,q) in ziped
    ])
    return 0 < diff_count and diff_count < 5

def f_5():
    f = open('program.c', encoding='utf-8')
    history = []
    sim_line_count = 0
    for line in f.readlines():
        line = line.replace('\n', '')

        if (len(line) < 20):
            continue

        for line_prev in history:
            if (is_similar_pair(line, line_prev)):
                sim_line_count+=1
                print(line_prev)
                print(line)
                print('')

        history.append(line)
    print(sim_line_count)

# f_5()

# (6)

# (7)

# コンボ終了時評価
def end_of_db(history, temp_db_i, temp_dl_cnt):
    if (temp_dl_cnt >= 4):
        for i in range(temp_db_i, temp_db_i + temp_dl_cnt):
            print(history[i])

def f_7():
    f = open('program.c', encoding='utf-8')
    history = []
    # temp_dup_block_index
    temp_db_i = None
    # temp_dup_line_count
    temp_dl_cnt = 0

    end_check = False

    # 読んでいく
    for line in f.readlines():
        line = line.replace('\n', '')

        # コンボ継続中
        if (temp_db_i != None):
            # 続くか？
            if (len(history) > temp_db_i + temp_dl_cnt):
                if (line == history[temp_db_i + temp_dl_cnt]):
                    temp_dl_cnt+=1
                else:
                    end_check = True
            else:
                end_check = True

            if end_check:
                end_check = False
                end_of_db(history, temp_db_i, temp_dl_cnt)
                if (line in history):
                    temp_db_i = history.index(line)
                    temp_dl_cnt = 1
                else:
                    temp_db_i = None
                    temp_dl_cnt = 0

        # コンボ開始できるか？
        elif (line in history):
            temp_db_i = history.index(line)
            temp_dl_cnt+=1

        # 読み込み記録
        history.append(line)

f_7()
