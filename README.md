# ImageProcessing2

・行った処理
カメラから読み込んだ映像をグレースケール方式に変換した後,opencvに搭載されているcannyアルゴリズムを用いてエッジを検出する.

・実行の仕方
cv2.VideoCaptureを用いて画像を取得する.
2本のトラックバーを閾値として設定し,それぞれが設定した範囲内で移動できるようにする.
取得した画像をグレースケールに変換する.
Canny法を用いてエッジを検出する.この時設定される閾値はトラックバーの値が反映される.
作成されたエッジ画像をウィンドウで表示する.
これを'Esc'もしくは'q'が押されるまで繰り返す.
どちらかのキーが押されたときウィンドウを閉じる.

・依存ライブラリ
Python 3.6.5
opencv 3.4.1
numpy  1.14.5

参考サイト
Canny法によるエッジ検出 — OpenCV-Python Tutorials 1 documentation:
http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_canny/py_canny.html

(Cannyを扱う上での基礎知識)

【Python/OpenCV】Cannyアルゴリズムで輪郭検出:
https://algorithm.joho.info/programming/python/opencv-canny-edge-detecte-py/

（グレースケールへの変換・エッジの検出のコード等）
