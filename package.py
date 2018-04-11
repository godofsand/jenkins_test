# -*- coding: utf-8 -*-

name = 'qtpy_test'

version = '0.1.0'


description = 'qtpy_test'

authors = ['jaekwang.choi']

requires = [
]

def commands():
    env.PATH.append("{root}/bin")

tests = {
    "pyqt4": "rez-env vp_qtpy_dev pyqt4 -c art_publish_qtpy_pyqt4",
    "pyqt5": "rez-env vp_qtpy_dev pyqt5 -c art_publish_qtpy_pyqt5",
    "pyside": "rez-env vp_qtpy_dev pyside -c art_publish_qtpy_pyside",
    "pyside2": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test12": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test13": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test14": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test15": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test16": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test17": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test18": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test19": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test20": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test21": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test22": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test23": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test24": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test25": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",
    "test26": "rez-env vp_qtpy_dev pyside2 -c art_publish_qtpy_pyside2",

}

uuid = 'repository.qtpy_test'
