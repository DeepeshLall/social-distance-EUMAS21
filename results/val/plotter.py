#!/usr/bin/env python

import csv
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

opt = []
alg = []

opt_std = []
alg_std = []

file_name = sys.argv[1]
rel_addr = ""
if len(file_name.split(".csv")[0].split("/")) > 1:
    rel_addr = file_name.split("csv/"+file_name.split(".csv")[0].split("/")[-1] + ".csv")[0]
output_file = rel_addr + "plots/" + \
    file_name.split(".csv")[0].split("/")[-1] + ".png"

opt_tmp = []
alg_tmp = []
m = 3
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        if int(row[0]) == m:
            opt_tmp.append(float(row[1]))
            alg_tmp.append(float(row[2]))
        else:
            m = int(row[0])
            opt_tmp = np.array(opt_tmp)
            alg_tmp = np.array(alg_tmp)
            opt.append(np.mean(opt_tmp))
            alg.append(np.mean(alg_tmp))
            opt_std.append(np.std(opt_tmp))
            alg_std.append(np.std(alg_tmp))
            opt_tmp = []
            alg_tmp = []
opt_tmp = np.array(opt_tmp)
alg_tmp = np.array(alg_tmp)
opt.append(np.mean(opt_tmp))
alg.append(np.mean(alg_tmp))
opt_std.append(np.std(opt_tmp))
alg_std.append(np.std(alg_tmp))

opt = np.array(opt)
alg = np.array(alg)
opt_std = np.array(opt_std)
alg_std = np.array(alg_std)
xticks = np.array(range(3, 3+len(opt)))

plt.plot(xticks, opt, '-', color='dodgerblue', label='Optimal')
plt.fill_between(xticks, opt - opt_std, opt +
                 opt_std, color='dodgerblue', alpha=0.3)
plt.plot(xticks, alg, '-', color='orange', label='Approximate')
plt.fill_between(xticks, alg - alg_std, alg +
                 alg_std, color='orange', alpha=0.3)
plt.xlabel('slots')
plt.ylabel('Social Wellfare')
plt.title('Total Social wellfare vs number of slots')
plt.legend(loc='upper left')
plt.grid()
# plt.show()
plt.savefig(output_file)
