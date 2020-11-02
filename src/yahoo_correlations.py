#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:48:27 2020

@author: charly
"""
import yahoo_io as io
import seaborn as sns
import matplotlib.pyplot as plt

dir_name = './data/'

target = 'Close_BTC_USD'
#labels = ['BTC', 'CAC40', 'Crude', 'Gold', 'DJI', 'S&P', 'NASDAQ', '$/CNY', '$/€', '$/¥']


def corr_plots(df):# Build correlation maps
    '''Builds correlation maps by dispatching to reg_plots() kde_plots() & corr_map()'''
    volume_cols=[]
    close_cols=[]
    for col in df.columns:
        if col.startswith( 'Vol_' ):
            volume_cols.append(col)
        elif col.startswith('Close_'):
            close_cols.append(col)
    volume_cols.append(target)

    # Linear regression plots
    reg_plots(df, close_cols)
    reg_plots(df, volume_cols)

    # KDE plots
    kde_plots(df, [target, 'Close_DJI_USD','Close_GC=F_USD','Close_EUR=X'])
    kde_plots(df, [target, 'Vol_BTC_USD','Vol_GSPC_USD','Vol_DJI_USD'])

    # Correlation heatmaps
    # correlation heatmap with quotes
    corr_map(df[close_cols], 'Close Heatmap')
    # correlation heatmap with volume
    corr_map(df[volume_cols], 'Volume Heatmap')
    #correlation among all predictors
    corr_map(df, 'Predictor Heatmap')


def corr_map(df, title):
    '''Builds a red->blue correlation map for a given dataframe'''
    size = 18
    linewidths = 1.5
    f,ax = plt.subplots(figsize=(size, size))
    ax.set(title  = title,
           xlabel = "security",
           ylabel = "security")
    sns.heatmap(df.corr(),
                annot      = True,
                linewidths = linewidths,
                fmt        = '.2f',
                ax         = ax,
                cmap       = "coolwarm",
                center     = 0.0);
    plt.show()


def reg_plots(df, column_list):
    ''' linear regression fit & univariate KDE curves'''
    color = '#d11928'
    for col in column_list:
        sns.jointplot(df[target],
                  df[col],
                  kind="reg",
                  color=color);
    plt.show()


def kde_plots(df, column_list):
    '''Build joint pdfs'''
    sns.set(style="white")
    g = sns.PairGrid(df[column_list], diag_sharey=False)
    g.map_lower(sns.kdeplot, cmap="Blues_d")
    g.map_diag(sns.kdeplot, lw=3);
    plt.show()


if __name__ == '__main__':
    prefix = 'merged_raw'
    df = io.load_csv(prefix)

    print(df.describe().transpose())

    # Drop rows with empty cells (impute later)
    df = df.dropna()
    df = df.drop(['Unnamed: 0'], axis=1)

    corr_plots(df)
