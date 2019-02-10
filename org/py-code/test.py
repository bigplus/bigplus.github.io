#!/usr/bin/env python
# encoding:utf-8
import matplotlib
import numpy as np
import scipy.stats as stats
from IPython.core.pylabtools import figsize
from matplotlib import pyplot as plt

import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='product', )
cur = conn.cursor()

aa = cur.execute(
    "select 200 + 200 * floor((deal_money-200)/200), count(1) from product_deal where deal_time >= '2017-05-04 00:00:00' and deal_time <= '2017-05-05 00:00:00' group by floor((deal_money-200)/200)"
)
# print aa

info = cur.fetchmany(aa)

# 原始数据
x1=[]
y1=[]

x = range(0, 10200, 200)
kv = {}
for ii in info:
    print ii
    kv[ii[0]] = ii[1]
    x1.append(ii[0])
    y1.append(ii[1])

y = []
for item in x:
    if item in kv.keys():
        y.append(kv[item])
    else:
        y.append(0)

for tp in zip(x, y):
    print tp[ 0 ], ' : ', tp[1]
cur.close()
conn.commit()
conn.close()


# matplotlib.use('Agg')

figsize(15, 10)

# x = np.linspace(0, 1, 100)

# For the already prepared, I'm using Binomial's conj. prior.
for k in range(8):
    x = x
    y = y
    plt.plot(x, y, label="abc" + k)
    plt.fill_between(x, 0, y, color="#348ABD", alpha=0.4)
    plt.vlines(0.5, 0, 4, color="k", linestyles="--", lw=1)

    leg = plt.legend()
    leg.get_frame().set_alpha(0.4)
    plt.autoscale(tight=True)

plt.suptitle("deal analysis", y=1.02, fontsize=14)

plt.tight_layout()
plt.savefig('plotxx.png', dpi=60)
print '<plotxx.png>'

# plt.plot(x, y, 'r', label='deal_cnt')
# plt.plot(x1, y1, 'b', label='deal_cnt2')

# plt.savefig('plotxx.png', dpi=60)
# print '<plotxx.png>'
