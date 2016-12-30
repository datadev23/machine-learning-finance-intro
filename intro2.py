#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd


def get_max_close(symbol):
    df = pd.read_csv('data/{}.csv'.format(symbol))
    return df['Close'].max();


def test_run():

# function called by test run

    for symbol in ['IBM']:
        print 'Max close'
        print symbol
	print get_max_close(symbol)


if __name__ == '__main__':
    test_run()

			
