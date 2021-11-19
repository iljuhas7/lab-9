#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rev_key(dct):
    dct_new = dict()
    for i, v in dct.items():
        for w in v:
            dct_new[w] = dct_new.get(w, []) + [i]

    return dct_new


print(rev_key({1: 'acc', 2: 'cab', 3: 'ccb'}))
