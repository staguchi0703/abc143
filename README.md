# at_coder_template
## 目的
VScodeでat_coderのABCに参加するための準備

## 使い方
1. github上で`templete`をクローンしたリポジトリを作成し、参加コンテストの名前を付ける。
   * レポジトリを新規作成する画面に遷移した際に、他のリポジトリを取り込むリンクがあるので、そこから作成すると早い。 
2. ローカルに複製する。　`git clone {repo}`
   * 複製するとローカルリポジトリのディレクトリに自動で飛ぶ。
   * そこで`code .`すれば、そのまま今回のコンテストに必要なディレクトリだけを持ったworkingspaceが立ち上がる。
3. テストケースの値を各問題フォルダの`X_input.txt`にペースト
4. 回答をX.pyに記入
5. 実行して動作確認する。terminalからのpython実行をキーバインドするのが〇
6. cwdは、クローンしてきたリポジトリの先頭にいること（フォルダA~Fが見えているところ）。
7. 19行目からを回答へ投げる
8. 終わったらpushして公開する

## 回答

### D
#### 感想
* 今回も計算オーダを減らす方法が分からず撃沈
* 他の人の回答みたら二分法でうまくやってるっぽい
* numpyのwhere使って数えても計算速度が足りなかった
* 
#### 気づき
* リストから組み合わせを考えるとき、重複をさけたり、大小関係を使ったりする場合のポイント
  * forでindexを回して、最後にリストから取り出したほうが便利
  * indexの重複可否を決められる
  * indexの大小関係を使える
  * ネストしたループを作るとき、以下のように記述すると重複を避けられる

```python3
    for i in range(N):
        for j in range(i+1, N):
```

* 二分法

  * 使い方
    * `bisect_right()`と`bisect()`は同じ操作
    * 今回の問題は同じ値でも棒は区別できるので値の重複は残すため`bisect_left()`を使用する


``` python
from bisect import bisect
from bisect import bisect_right
from bisect import bisect_left

lst = [0, 3, 3, 3, 5]

# bisect
#   値をリストに
#   差し込む位置を返してくれます。
bisect(         lst, 3)  # 4
bisect_right(   lst, 3)  # 4
bisect_left(    lst, 3)  # 1

```

 * 二分法標準ライブラリのソース


``` python
''' bisect source code  '''
def bisect_left(a, x, lo=0, hi=None):
    """ Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e < x, and all e in 
    a[i:] have e >=x. so if x already appears in the list, a.insert(x) will insert just before 
    the leftmost x already there.

    Optional args lo and hi bound the slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

#### TODO

* [x] 今回の二分法の解き方理解

* [ ] 過去問のDを練習する
