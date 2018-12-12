#!/usr/bin/env python
# coding: utf-8
""" Tanemaki """
from codecs import open as codecs_open
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with codecs_open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='tanemaki',
    version='0.1.1',
    description='モグ雄になれるPythonライブラリ',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/curious-eyes/tanemaki.lib.py',
    author='okamoto',
    author_email='shuhei.okamoto@gmail.com',
    license='MIT',
    # 依存ライブラリは下のリストを元にinstallされる
    install_requires=[],
    extras_require={},
    keywords='tanemaki',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    # 今回コマンドを作ったのでconsole_scriptsを記述している
    entry_points={
        "console_scripts": [
            "tanemaki=tanemaki.tanemaki:Tanemaki",
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
