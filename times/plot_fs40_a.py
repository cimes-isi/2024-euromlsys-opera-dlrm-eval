import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

networks = {
	'FatTree-Ring': [31.84568373, 4.611576088, 0.632813773],
	'FatTree-DPS': [32.29037947, 4.650869873, np.nan],
	'TopoOpt-Ring': [29.01723348, 4.215734099, 0.995540439],
	# 'Opera-Ring': [14.75572819, 3.668321778, 9.59904892],
	'Opera-DPS': [28.79300367, 3.942842538, 0.697230401],
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
plt.savefig('fs40_a.pdf', bbox_inches='tight', pad_inches=.15, dpi=600)
