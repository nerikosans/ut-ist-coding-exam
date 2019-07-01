import numpy as np
import scipy as sp
import math

# (COMMON) 解答です
# 19:23

# 数のテンプレート
num_dic = {
    0: ['****', '|  |', '*  *', '|  |', '****'],
    1: ['*', '|', '*', '|', '*'],
    2: ['****', '   |', '****', '|   ', '****'],
    3: ['****', '   |', '****', '   |', '****'],
    4: ['*  *', '|  |', '****', '   |', '   *'],
    5: ['****', '|   ', '*  *', '   |', '****'],
    6: ['*   ', '|   ', '****', '|  |', '****'],
    7: ['****', '   |', '   *', '   |', '   *'],
    8: ['****', '|  |', '****', '|  |', '****'],
    9: ['****', '|  |', '****', '   |', '   *'],
}

# 数字からテンプレートへ
def num_template(i):
    return num_dic.get(i)

# テンプレートから数字へ
def template_to_num(arr):
    for key in num_dic.keys():
        if arr == num_dic[key]:
            return key
    return None

# rows行2列の空白
def space(rows=5, cols=2):
    return [' ' * cols] * rows

# np.arrayをprint
# filenameを指定すると書き出し
def print_array(arr, filename=None):
    f = None
    if filename is not None:
        f = open(filename, 'w', encoding='utf-8')
        # clear
        f.write('')

    for row in arr:
        print(row)
        if f is not None:
            f.writelines(row + '\n')

    if f is not None:
        f.close()

# もっとも高い数字の高さ
def max_height(num_list):
    res = 0
    for num in num_list:
        res = max(res, len(num))
    return res

# 数字を結合
def concat_num(num_list):
    h = max_height(num_list)
    res = [''] * h
    for num in num_list:
        cols = len(num[0])
        num = num + space(cols=cols, rows=h)

        res = [
            res[i] + num[i]
            for i in range(h)
        ]

    return res

# 空列？
def is_spacecol_at(arr, col):
    for row in arr:
        row = row + (' ' * col)
        if row[col] is not ' ':
            return False

    return True

# 空行？
def is_spacerow(row):
    return row.replace(' ', '') is ''
def is_spacerow_at(arr, row):
    target = arr[row]
    return is_spacerow(target)

# 1個のテキストを空列で縦分割
def vertical_split(line):
    cols = len(line[0])

    h = max_height(line)
    num_list = []

    temp_col = None

    # 左から読んでいく
    for c in range(cols):
        # not 空列
        if not is_spacecol_at(line, c):
            if temp_col is None:
                temp_col = c

        # 数字エリア終わり
        else:
            if temp_col is not None:
                num_list.append([
                    row[temp_col:c]
                    for row in line
                ])
                temp_col = None

    # 終了処理
    if temp_col is not None:
        num_list.append([
            row[temp_col:]
            for row in line
        ])

    return num_list

# 文字を下にずらす
def pull_down(arr, offset=1):
    cols = len(arr[0])
    return space(cols=cols, rows=offset) + arr

# 文字の上にある空白をどかす
def trim_spacerow(arr):
    return list(filter(lambda row: not is_spacerow(row), arr))

# 数字numとtemplate_inputの類似度
# 4*5 のみ
def likelihood(num, template_input):
    t = num_template(num)
    s = template_input

    score = 0
    for y in range(5):
        s_row = s[y] + (' ' * 4)
        for x in range(4):
            if (t[y][x] is s_row[x]):
                score += 1
                continue
            if x <= 2:
                if t[y][x+1] is s_row[x]:
                    score += 0.5
                    continue
            if x >= 1:
                if t[y][x-1] is s_row[x]:
                    score += 0.5
                    continue

    return score / 20

# 最も似ている数字
def most_likely(template_input):
    # 1は例外
    if len(template_input[0]) <= 2:
        return 1

    max_like = 0
    max_i = None

    for i in range(2,10):
        temp_like = likelihood(i, template_input)
        if temp_like > max_like:
            max_like = temp_like
            max_i = i

    return max_i

def __main():
    return

if __name__ =='__main__':
    __main()
