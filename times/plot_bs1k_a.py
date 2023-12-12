import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

networks = {
	'FatTree-Ring': [71.60887296, 9.467728123, 2.082297029],
	'FatTree-DPS': [59.27763503, 8.107972154, np.nan],
	'TopoOpt-Ring': [59.77716488, 10.06130833, 2.963886174],
	# 'Opera-Ring': [14.70431911, 7.679978878, 10.01135384],
	'Opera-DPS': [61.83100473, 7.945408258, 1.276756268],
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
plt.savefig('bs1k_a.pdf', bbox_inches='tight', pad_inches=.15, dpi=600)
