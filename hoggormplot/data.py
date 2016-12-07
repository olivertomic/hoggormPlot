# -*- coding: utf-8 -*-
"""Import exampledata"""

from os import path as osp
import pandas as pd
DATADIR = osp.join(osp.dirname(osp.realpath(__file__)), 'exampledata')


def getOECD():
    return pd.read_table(osp.join(DATADIR, 'Cancer_men_perc.txt'), index_col=0)

def getA():
    return pd.read_table(osp.join(DATADIR, 'A.txt'), index_col=0)

def getB():
    return pd.read_table(osp.join(DATADIR, 'B.txt'), index_col=0)
