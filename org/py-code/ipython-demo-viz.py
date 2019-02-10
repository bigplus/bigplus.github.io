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
print aa

info = cur.fetchmany(aa)
for ii in info:
    print ii
cur.close()
conn.commit()
conn.close()

# matplotlib.use('Agg')

figsize(15, 10)

dist = stats.beta
n_trials = [0, 1, 2, 3, 4, 5, 8, 15, 50, 500]
data = stats.bernoulli.rvs(0.5, size=n_trials[-1])
x = np.linspace(0, 1, 100)

# For the already prepared, I'm using Binomial's conj. prior.
for k, N in enumerate(n_trials):
    sx = plt.subplot(len(n_trials) / 2, 2, k + 1)
    plt.xlabel("$p$, probability of heads") \
        if k in [0, len(n_trials)-1] else None
    plt.setp(sx.get_yticklabels(), visible=False)
    heads = data[:N].sum()
    y = dist.pdf(x, 1 + heads, 1 + N - heads)
    plt.plot(x, y, label="observe %d tosses,\n %d heads" % (N, heads))
    plt.fill_between(x, 0, y, color="#348ABD", alpha=0.4)
    plt.vlines(0.5, 0, 4, color="k", linestyles="--", lw=1)

    leg = plt.legend()
    leg.get_frame().set_alpha(0.4)
    plt.autoscale(tight=True)

plt.suptitle(
    "Bayesian updating of posterior probabilities", y=1.02, fontsize=14)

plt.tight_layout()
plt.savefig('plotxx.png', dpi=60)
print '<plotxx.png>'
