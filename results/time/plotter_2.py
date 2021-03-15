#!/usr/bin/env python

import csv, sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plot = []

plot_std = []

file_name = sys.argv[1]
rel_addr = ""
if len(file_name.split(".csv")[0].split("/")) > 1:
    rel_addr = file_name.split("csv/"+file_name.split(".csv")[0].split("/")[-1] + ".csv")[0]
output_file = rel_addr + "plots/" + file_name.split(".csv")[0].split("/")[-1] + "_2.png"

plot_tmp = []
m=3
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        if int(row[0]) == m:
            t_opt = float(row[1])
            t_alg = float(row[2])
            reduction = (t_opt - t_alg)/t_opt*100
            plot_tmp.append(reduction)
        else:
            m = int(row[0])
            plot_tmp = np.array(plot_tmp)
            plot.append(np.mean(plot_tmp))
            plot_std.append(np.std(plot_tmp))
            plot_tmp = []
plot_tmp = np.array(plot_tmp)
plot.append(np.mean(plot_tmp))
plot_std.append(np.std(plot_tmp))
plot = np.array(plot)
plot_std = np.array(plot_std)
xticks = np.array(range(3,3+len(plot)))

plt.plot(xticks, plot, '-', color='dodgerblue', label='% Reduction in Time')
plt.fill_between(xticks, plot - plot_std, plot +
                 plot_std, color='dodgerblue', alpha=0.3)
plt.xlabel('number of slots')
plt.ylabel('% Reduction Time')
plt.title('% Reduction Time vs number of slots')
plt.legend(loc='upper left')
plt.grid()
# plt.show()
plt.savefig(output_file)
