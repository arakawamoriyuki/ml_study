# ml_bottle

- 超軽量フレームワーク[bottle](http://bottlepy.org/docs/dev/index.html)に乗せた機械学習環境と画像解析API

## 動作環境

```
$ python --version
Python 2.7.13 :: Anaconda 4.3.0 (x86_64)
or
Python 3.6.0 :: Anaconda 4.3.0 (64-bit)
$ python
>>> import tensorflow as tf
>>> tf.__version__
'1.0.0'
>>> import bottle
>>> bottle.__version__
'0.12.13'
```

## endpoints

|endpoint|method|description|
|:-:|:-:|:-:|
|/|GET|ルーティング一覧|
|/inception|GET|パラメータimageに画像urlを乗せて分類|
|/inception|POST|パラメータimageに画像binaryを乗せて分類|
|/inception/test|GET|inception apiを試すview|

## local run

localで起動する場合、下記環境が必要になります。(dockerで良ければlocal環境は必要ありません)

- bottle
- requests
- numpy
- six
- tensorflow

bottleとrequestsはpipでinstallできます。
numpyやsixなどは機械学習環境をまとめた[anaconda](https://www.continuum.io/downloads)で環境を作ります。
tensorflowは[github](https://github.com/tensorflow/tensorflow)に従って環境を作ります。

```
$ python server.py
```

## local docker run

- linux (Linux cd4ac837b33e 4.4.14-moby #1 SMP Wed Jun 29 10:00:58 UTC 2016 x86_64 GNU/Linux)
- anaconda (Python 3.6.0 :: Anaconda 4.3.0 (64-bit))
- tensorflow (1.0.0)
- bottle (0.12.13)

### build and run

```
$ docker build --rm -t ml-bottle .
$ docker run -d -p 8080:8080 --name ml-bottle ml-bottle
```
