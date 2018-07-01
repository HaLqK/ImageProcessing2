# ImageProcessing2

・行った処理　　
<br>
カメラから読み込んだ映像をグレースケール方式に変換した後,opencvに搭載されているcannyアルゴリズムを用いてエッジを検出する.
<br>
・実行の仕方　　
<br>
cv2.VideoCaptureを用いて画像を取得する.<br>
2本のトラックバーを閾値として設定し,それぞれが設定した範囲内で移動できるようにする.<br>
取得した画像をグレースケールに変換する.<br>
Canny法を用いてエッジを検出する.この時設定される閾値はトラックバーの値が反映される.<br>
作成されたエッジ画像をウィンドウで表示する.<br>
これを'Esc'もしくは'q'が押されるまで繰り返す.<br>
どちらかのキーが押されたときウィンドウを閉じる.<br>
<br>
・依存ライブラリ
<br>　　
Python 3.6.5
<br>
opencv 3.4.1　　
<br>
numpy  1.14.5　　
<br>
参考サイト<br>　　
Canny法によるエッジ検出 — OpenCV-Python Tutorials 1 documentation:
http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_canny/py_canny.html
<br>　
(Cannyを扱う上での基礎知識)
<br>
【Python/OpenCV】Cannyアルゴリズムで輪郭検出:　　
https://algorithm.joho.info/programming/python/opencv-canny-edge-detecte-py/
<br>　
（グレースケールへの変換・エッジの検出のコード等）
