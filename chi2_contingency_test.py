# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:39:04 2018

@author: Administrator
"""

from scipy.stats import chi2_contingency

def test_chi2_contingency():
    #双向表/列联表
    table = [[120, 110], [150, 170]]
    chi2, p, dof, expected = chi2_contingency(table, correction=False)
    print("P=", p)