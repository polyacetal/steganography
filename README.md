# steganography
これは画像に暗号を隠すためのツールです  

## 使い方
1.隠すための画像を用意する  
2.同じ大きさで黒い(#000000)背景に白い(#ffffff)文字で暗号文を描いた画像を用意する  
3.$ python3 encoder.py (1のファイル) (2のファイル)  を実行する  
4.出力されたhiden.pngに暗号が隠されています  

逆に暗号文を見たい場合は  
$ python3 decoder.py hiden.png  を実行してください  

##必要なもの
以下のものがない場合は適宜追加してください
sys  
math  
numpy  
numpy  
