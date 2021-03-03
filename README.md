# pixel_art(ドット絵加工のPythonプログラム)

## 資料
https://note.nkmk.me/python-opencv-imread-imwrite/

## 使い方
※仮想環境については下記ライブラリが入っている環境があれば、仮想環境構築はスキップして問題ないです。
[numpy, opencv-python, opencv-contrib-python]

### リポジトリのクローン。
git clone <url>

### クローンしたディレクトリに移動。
cd pixel_art

### 仮想環境の構築。
※指定のライブラリが入っていればスキップ可。
python3 -m venv 任意の環境名

### 仮想環境(venv)を起動。
--Mac, Linux--
source 仮想環境名/bin/activate
--windows--
./仮想環境名/Scripts/activate

### 実行。引数に画像をクリック&ドロップ。
python mosaic.py "画像"

※変換後の画像は「converted_img」ディレクトリに格納されます。
　→ファイル名は「元の画像名_converted」になります。

### 荒さ、色の調節
mosaic.pyの71行目(dst = (img, 0.3, 10))で調整する。
pixel_artメソッドの"alpha = 画像の荒さ"、"K = 色数"となります。
初期値はalpha=0.3、K=10色となっています。お好みに調整ください。
