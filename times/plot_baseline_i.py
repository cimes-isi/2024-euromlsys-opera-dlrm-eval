import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

networks = {
	'FatTree-Ring': [10.75120609, 1.497664799, 0.721784106],
	'FatTree-DPS': [10.7467046, 1.629890511, np.nan],
	'TopoOpt-Ring': [11.49997694, 2.187027134, 0.754955793],
	# 'Opera-Ring': [11.91286254, 1.481644282, 4.92018678],
	'Opera-DPS': [11.92637766, 1.505148802, 0.56095188],
}

# ----------------------------------------------------------------------

nodes = [16, 128, 1024]
x = np.arange(len(nodes)) # the label locations
width = 0.15 # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')
fig.set_size_inches(6, 3.5)

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
plt.savefig('baseline_i.pdf', bbox_inches='tight', pad_inches=.15, dpi=600)
