import numpy as np
import scipy as sp
import math

# (7) だよ

def convert_eng_to_10():
    eng_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90
    }

    eng_dict_order = {
        'hundred': 100,
        'thousand': 1000
    }

    input_str = input('Input (英語) >')

    words = input_str.split(' ')

    num_10 = 0
    temp = 0

    for w in words:
        if w in eng_dict:
            temp += eng_dict[w]
        elif w in eng_dict_order:
            num_10 += temp * eng_dict_order[w]
            temp = 0

    num_10 += temp

    print(num_10)
    return num_10

convert_eng_to_10()
