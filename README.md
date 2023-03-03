# What is "MEMOPRO"

本アプリは入力した文字数をカウントするWebアプリケーションである。

# Description

本アプリでは、レポートやエントリーシートなどの字数制限がある文章を作成するときに活躍します。
タイトルとテキストの入力、テキストの文字数を赤文字で出力。
なお、本プロダクトの開発には、Djangoを用いたフレームワークが採用されました。

＊空白、改行は含まない。

＊公開していない

＊セキュリティ対策のためSECRET_KEYは***で隠している。

# DEMO


作成ウェブページ

![alt](memo.gif)


# Requirement

* Windows10 Home
* conda == 22.9.0
* conda-build == 3.22.0
* python == 3.9.13
* Django==4.1.6
* django-environ==0.9.0
* ubuntu-advantage-tools==8001
* ubuntu == 20.04
* virtualenv==20.19.0

# Installation

[Anaconda](https://www.anaconda.com/products/distribution)のサイトのダウンロードページからWindows用のPython3.9 64bit Graphical Installerをダウンロードする(Anacondaをインストール完了することでpythonの利用可能)。

1. ubuntuのダウンロード(ubuntu 20.04 LTS)
2. Djangoを用いて開発を行うにあたって仮想環境構築。 [こちら](https://www.sejuku.net/blog/68398)が参考サイト。

Djangoの始め方仮想環境構築などは[udemy](https://www.sejuku.net/blog/68398)を利用して勉強した。

[この動画](https://www.sejuku.net/blog/68398)を見れば誰でも環境の構築が出来ると思う。


virtualenvのインストール
```bash
sudo pip install virtualenv
```

仮想環境を構築
```bash
virtualenv -p python3 venv
```

仮想環境の立ち上げ
```bash
source venv/bin/activate
```

Djangoのインストール>>>djangoの[公式サイト](https://docs.djangoproject.com/ja/4.0/)
```bash
pip install Django
```


# Usage


```bash
git clone https://github.com/MEMOPRO/~

python manage.py runserver
```


# Author


* Sora Nakaza
* NIT
* s202065@nishitech.ac.jp

# License

"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).