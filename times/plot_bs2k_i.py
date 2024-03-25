import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

networks = {
	'FatTree-Ring': [42.76383511, 5.803371641, 2.360573877],
	'FatTree-DPS': [42.77754719, 5.84928628, np.nan],
	'TopoOpt-Ring': [47.19520524, 8.538851385, 4.524203757],
	# 'Opera-Ring': [np.nan, 5.876956664 5.26670098],
	'Opera-DPS': [47.0855251, 5.904235604, 2.079292441],
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
plt.savefig('bs2k_i.pdf', bbox_inches='tight', pad_inches=.15, dpi=600)
