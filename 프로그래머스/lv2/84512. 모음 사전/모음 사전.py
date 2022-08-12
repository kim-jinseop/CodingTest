from itertools import product
def solution(word):
    answer = 0
    arr = ['','A','E','I','O','U']
    box = list(set(map(''.join,product(arr,repeat=5))))
    box.sort()
    return box.index(word)