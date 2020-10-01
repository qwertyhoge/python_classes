# 目標
Pythonによる文字列処理に慣れる。  
文字列のソースとしてテキストファイルの扱いに触れ、  
splitによる分割や、正規表現による文字列処理について学ぶ。

各課題の難易度を+の個数で表した。  
厳密ではないが、参考程度に。

# プログラム例(見本)
見本となるプログラム例をexamples/に並べておいた。  
どうしても処理方法が思い浮かばない場合や、  
書いたものが適切な処理方法かどうかに不安がある場合に見るといい。

# 課題1 +
テキストファイルの文字列を読み取る。  
data/hoge_single_line.txt内の文字列を全て表示するプログラムを作成する。

# 課題2 +
テキストファイルの文字列を行ごとに読み取る。  
data/hoge_multi_line.txtの各行について、  
行番号とその行にある文字列を表示する。

# 課題3 +
テキストファイルを書き込む。
data/new_hoge.txtといったテキストファイルを新たに作成し、  

```
hoge
hoge
fuga
fuga
hoge
fuga
fuga
```

などと書き込む。

# 課題4 ++
CSVファイルの数値で計算をする。  
data/numbers.csvを読み、  
各行で、カンマ区切りで書いてある数値群の総和を出力する。  
splitを使うとよい。

なお、カンマの前後のスペース等について対策はしなくてよい。  
(必ず`1,2,3`のような形と考えてよい。)

# 課題5 ++++
正規表現を用いて、  
data/sentences.txtの各行について、  
`There is`または`There are`で始まり、  
`.`で終わる文になっているかどうか(文法の正しさは問わない)判定を行い、  
なっていれば  
`T: There is an apple.`  
なっていなければ  
`F: There were an old man.`  
のように表示する。

正規表現のパターン指定のときには単純な文字列`""`ではなく  
`r""`と、開始ダブルクォート前に`r`を付けなければならないことに注意。

# 課題6 +++
正規表現を用いて、  
data/id_links.txtに含まれているユーザーネームを全て出力する。  
`@someName`のように、`@`で始まって  
アルファベットだけ(大文字小文字どちらでも)がその後に続くものをユーザーネームとする。