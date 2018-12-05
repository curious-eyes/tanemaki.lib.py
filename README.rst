========
Tanemaki
========
This still is not the official Tanemaki library.

まだタネマキ非公認ライブラリです

Join the Discussion
===================
If you want to get involved in the community, feel free to join Tanemaki.

何かあれば、タネマキまで。

============
Dependencies
============
Tanemaki is compatible with Python 3.6, 3.5 and 2.7.

============
Installation
============

Installing from Source
======================

仮想環境の利用を推奨します。

::

    $ python -m venv ./venv
    $ source ./venv/bin/activate

インストール実行

::

    $ git clone https://github.com/curious-eyes/tanemaki.lib.py.git
    $ pip install -e .

==========
How to Use
==========

コマンドラインツール
==================================

::

    $ tanemaki
    2011年12月01日生まれなので、もう 7 年目もぐー

    $ tanemaki --plan
    詳しくは https://tane-maki.net/pricing/ を参照もぐー
    


Pythonライブラリ
==================================

import して使うと、さらに多機能です。

::

    $ python
    >>> from tanemaki import Tanemaki
    >>> t = Tanemaki()
    >>> t      # タネマキの情報を表示します
    2011年12月01日生まれなので、もう 7 年目もぐー
    >>>
    >>> len(t)    # 営業開始からの経過日数
    2561
    >>> Tanemaki.say_moguo('エアコンを取り替える')     # もぐおになれます
    'エアコンを取り替えるもぐー'
    >>>
    >>> t + 'おかも'
    'おかも さん、いらっしゃいもぐー'
    >>> t + 'モグ子'
    'モグ子 さん、いらっしゃいもぐー'
    >>> t - 'おかも'
    'おかも さん、またおいでもぐー'
    >>> t - 'おかも'
    'すでに おかも さんは帰ってるもぐー'
