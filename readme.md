# ml study

- ml_bottle: docker runだけで画像分類を試す
- workspace: 1ファイルで完結の機械学習サンプル群

## 環境 Anaconda in Python

- 主要ライブラリをオールインワンでインストール
- condaというパッケージ管理システム入り(pipの代わり)
- condaでバンージョン管理も可(pyenvの代わり)
- condaで仮想環境管理も可(virtualenv/venの代わり)

1. [anaconda](https://www.continuum.io/downloads#osx)公式からでインストール
2. インストールした場所によるがインストールすると下記にnumpyなど機械学習に必要な環境が作られる。

```
/anaconda
or
~/anaconda
```

```
$ /anaconda/bin/python --version
Python 2.7.13 :: Anaconda 4.3.0 (x86_64)
or
Python 3.6.0 :: Anaconda 4.3.1 (x86_64)
$ /anaconda/bin/pip list | grep numpy
numpy (1.11.3)
numpydoc (0.6.0)
$ /anaconda/bin/conda list | grep numpy
numpy                     1.11.3                   py27_0
numpydoc                  0.6.0                    py27_0
```

3. 現system環境と競合(pythonコマンドなど)するので使いたいときだけPATH通したほうが良い。

```
$ vi ~/.zshrc
```

```
## path functions
#
path_append ()  { path_remove $1; export PATH="$PATH:$1"; }
path_prepend () { path_remove $1; export PATH="$1:$PATH"; }
path_remove ()  { export PATH=`echo -n $PATH | awk -v RS=: -v ORS=: '$0 != "'$1'"' | sed 's/:$//'`; }

~~~

## anaconda
#
ANACONDA_PATH = /anaconda/bin
anaconda_active () {
  path_prepend $ANACONDA_PATH
}
anaconda_deactive () {
  path_remove $ANACONDA_PATH
}
```

```
$ python --version
Python 2.7.11
$ anaconda_active
$ python --version
Python 2.7.13 :: Anaconda 4.3.0 (x86_64)
$ anaconda_deactive
$ python --version
Python 2.7.11
```

## 分類サンプル

- workspace/classify

```
$ python logistic_regression.py
$ python logistic_regression_regularized.py
```

## 回帰サンプル

- workspace/regression

```
$ python gradient_descent_single.py
$ python gradient_descent_multi.py
$ python normal_equation.py
```

## 強化学習サンプル

- workspace/reinforcement_learning

### keras-rl

1. DQN(強化学習)評価用のプラットフォーム、OpenAiGymをinstall

```
$ git clone http://github.com/openai/gym
$ cd gym
$ pip install -e .
```

2. DQNなどの深層強化学習のアルゴリズムを実装したライブラリ、keras-rlをinstall

```
$ pip install keras-rl h5py
```

```
$ python workspace/reinforcement_learning/keras/dqn_cartpole.py
$ python workspace/reinforcement_learning/keras/ddpg_pendulum.py
```

## OpenAiUniverse

```
$ git clone http://github.com/openai/universe
$ cd universe
$ pip install -e .
$ xcode-select --install
$ pip install numpy incremental zbarlight
$ brew install libjpeg-turbo golang
```

```
$ python workspace/reinforcement_learning/universe/flashgames_DuskDrive-v0.py
```
