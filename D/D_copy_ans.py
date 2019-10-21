# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
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
from bisect import bisect_left
 
N = int(input())
Lmat = [int(n) for n in input().split()]
Lmat.sort()
 
sum = 0

for i in range(N):
    for j in range(i + 1, N):
        sum += bisect_left(Lmat, Lmat[i]+Lmat[j]) - (j + 1)
print(sum)