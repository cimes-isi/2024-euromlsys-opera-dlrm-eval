import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

networks = {
	'FatTree-Ring': [21.40779084, 2.932967665, 1.197608688],
	'FatTree-DPS': [21.3631927, 3.649059119, np.nan],
	'TopoOpt-Ring': [22.91724959, 4.423665567, 1.66223183],
	# 'Opera-Ring': [np.nan, 2.952563866, 5.02768406],
	'Opera-DPS': [23.81179717, 2.975209126, 1.06635044],
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
plt.savefig('bs1k_i.pdf', bbox_inches='tight', pad_inches=.15, dpi=600)
