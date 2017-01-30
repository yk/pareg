#!/usr/bin/env python3

from collections import OrderedDict
import numpy as np
from scipy.stats import spearmanr


def main():
    lines = []
    try:
        print('paste stuff')
        while(True):
            l = input('')
            l = l.strip()
            if len(l) > 0:
                lines.append(l)
    except:
        pass
    lines = [l.split() for l in lines]
    for l in lines:
        l[-1] = l[-1].split('/')[0]
    lines = [[t.split('=') for t in l] for l in lines]
    vals = OrderedDict()
    for l in lines:
        for k, v in l:
            if k not in vals:
                vals[k] = []
            if v == 'True':
                v = 1.
            if v == 'False':
                v = 0.
            vals[k].append(v)
    vals = {k: v for k, v in vals.items() if len(set(v)) > 1}
    values = list(zip(*vals.values()))
    keys = list(vals.keys())
    labels = []
    for vl in values:
        print()
        for k, v in zip(keys, vl):
            print('{}={}'.format(k, v), end=' ')
        i = input('>>> ')
        i = float(i)
        labels.append(i)

    X = np.array(values, dtype=np.float32)
    Y = np.array(labels, dtype=np.float32)

    print()
    print('Linear Regression:')
    w = np.linalg.lstsq(X, Y)[0]
    kw = list(zip(keys, w))
    kw = sorted(kw, key=lambda x: np.abs(x[1]), reverse=True)
    for k, wk in kw:
        print('{}: {}'.format(k, wk))

    print()
    print('Rank Correlation:')
    w = spearmanr(X, Y)[0][:-1, -1]
    kw = list(zip(keys, w))
    kw = sorted(kw, key=lambda x: np.abs(x[1]), reverse=True)
    for k, wk in kw:
        print('{}: {}'.format(k, wk))

    XY = sorted(list(zip(X, Y)), key=lambda x: x[1], reverse=True)
    best_label = XY[0][1]
    print()
    print('Best Configs (label = {}): '.format(best_label))
    for x, y in XY:
        if y != best_label:
            break
        for k, v in zip(keys, x):
            print('{}: {}'.format(k, v), end=' ')
        print()
if __name__ == '__main__':
    main()
