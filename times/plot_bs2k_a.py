import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

networks = {
	'FatTree-Ring': [117.7377696, 19.3474834, 4.066856619],
	'FatTree-DPS': [117.837123, 19.77750734, np.nan],
	'TopoOpt-Ring': [120.9366126, 18.85827285, 5.761501079],
	# 'Opera-Ring': [np.nan, np.nan, 10.15736564],
	'Opera-DPS': [123.278892, 15.65950903, 2.270694649],
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
plt.savefig('bs2k_a.pdf', bbox_inches='tight', pad_inches=.15, dpi=600)
