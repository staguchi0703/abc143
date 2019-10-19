# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\E\E_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
import numpy as np

N, M, L = [int(item) for item in input().split()]

load_list = []
for _ in range(M):
    load_list.append([int(item) for item in input().split()])

Q = int(input())

query_list = []
for _ in range(Q):
    query_list.append([int(item) for item in input().split()])


def search_dist(load_list, query):

    query = sorted(query)

    for load in load_list:
        if load[:1] == query:
            distance = load[2]
    return distance
    

def cunt_refill(L, )

for query in query_list:
    search_dist(load_list, query)




