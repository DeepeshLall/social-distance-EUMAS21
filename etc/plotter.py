#!/usr/bin/env python

import csv, sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]

output_file = "plots/" + file_name1.split(".csv")[0].split("/")[-1] + ".pdf"

plot1 = []
plot1_std = []
plot1_tmp = []
m = 3
with open(file_name1) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        if int(row[0]) == m:
            t_opt = float(row[1])
            t_alg = float(row[2])
            reduction = (t_opt - t_alg)/t_opt*100
            plot1_tmp.append(reduction)
        else:
            m = int(row[0])
            plot1_tmp = np.array(plot1_tmp)
            plot1.append(np.mean(plot1_tmp))
            plot1_std.append(np.std(plot1_tmp))
            plot1_tmp = []

plot2 = []
plot2_std = []
plot2_tmp = []
m = 3
with open(file_name2) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        if int(row[0]) == m:
            opt = float(row[1])
            alg = float(row[2])
            reduction = opt/alg
            plot2_tmp.append(reduction)
        else:
            m = int(row[0])
            plot2_tmp = np.array(plot2_tmp)
            plot2.append(np.mean(plot2_tmp))
            plot2_std.append(np.std(plot2_tmp))
            plot2_tmp = []
plot1_tmp = np.array(plot1_tmp)
plot1.append(np.mean(plot1_tmp))
plot1_std.append(np.std(plot1_tmp))
plot1 = np.array(plot1)
plot1_std = np.array(plot1_std)
print(plot1)
plot2_tmp = np.array(plot2_tmp)
plot2.append(np.mean(plot2_tmp))
plot2_std.append(np.std(plot2_tmp))
plot2 = np.array(plot2)
plot2_std = np.array(plot2_std)
print(plot2)
xticks = np.array(range(3, 3+len(plot1)))
print(xticks)
fig, (ax1, ax2) = plt.subplots(2, sharex=True)

ax1.plot(xticks, plot1, '-', color='dodgerblue', label='% Reduction in Time')
ax2.plot(xticks, plot2, '-', color='orange', label='Approximation factor')

ax1.fill_between(xticks, plot1-plot1_std, plot1+plot1_std, facecolor='dodgerblue', alpha=0.3)
ax2.fill_between(xticks, plot2-plot2_std, plot2+plot2_std, facecolor='orange', alpha=0.3)

# ax1.set_title('% Reduction Time vs number of slots')
# ax2.set_title('Approximation Factor vs number of slots')
# fig.suptitle("% Reduction Time and Approximation Factor vs number of slots")

ax1.set_ylabel("% Reduction Time")
ax2.set_ylabel("Approximation Factor")
ax2.set_xlabel("Number of slots")

ax1.grid(True)
ax2.grid(True)

plt.tight_layout()
plt.savefig(output_file)
# plt.show()
