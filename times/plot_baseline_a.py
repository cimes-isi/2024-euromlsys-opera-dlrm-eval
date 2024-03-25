import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

networks = {
	'FatTree-Ring': [36.81802843, 4.730327123, 0.723327503],
	'FatTree-DPS': [29.82630877, 4.083508833, np.nan],
	'TopoOpt-Ring': [31.05150943, 4.741642754, 1.431912859],
	# 'Opera-Ring': [np.nan, 3.844434627, 9.94618478],
	'Opera-DPS': [30.76346613, 4.162758327, 0.781648708],
}

# ----------------------------------------------------------------------

nodes = [16, 128, 1024]
x = np.arange(len(nodes)) # the label locations
width = 0.15 # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')
fig.set_size_inches(6, 3)

for attribute, measurement in networks.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1

ax.set_xticks(x + width * (len(networks) / 2 - 0.5), nodes)
ax.legend(loc='upper right', fontsize=10, frameon=False)
ax.set_yscale('log', base=2)
ax.set_ylim(ymin=0.5, ymax=128)
ax.get_yaxis().set_major_formatter(ScalarFormatter())
ax.set_xlabel('Nodes', fontsize=16)
ax.set_ylabel('Iteration Time (s)', fontsize=16)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)

# ----------------------------------------------------------------------

fig.tight_layout(pad=1.5)

# plt.show()
plt.savefig('baseline_a.pdf', bbox_inches='tight', pad_inches=.15, dpi=600)
