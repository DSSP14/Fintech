#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:53:49 2020

@author: charly
"""
import pandas as pd
import os

dir_name = '../data/'

def load_csv(prefix):
    '''Load csv data & return as a dataframe'''
    filename = os.path.join(dir_name, prefix + ".csv")
    return pd.read_csv(filename)


def write_csv(df, prefix):
    '''Write dataframe to csv'''
    filename = os.path.join(dir_name, prefix + ".csv")
    df.to_csv(filename, sep=',', encoding='utf-8')
    print(f'\ndataframe saved as {filename}\n')