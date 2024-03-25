import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(6, 3)

ax.set_xlabel('Nodes', fontsize=16)
ax.set_ylabel('Traffic Proportion', fontsize=16)

node_counts = ['16', '128', '1024']
traffic = {}
traffic["All-reduce traffic"] = [0.11821701960057965, 0.5174963326959043, 0.8956170479783089]
traffic["Other traffic"] = [1 - t for t in traffic["All-reduce traffic"]]
width = 0.5

bottom = np.zeros(3)
for lbl, weight_count in traffic.items():
    p = ax.bar(node_counts, weight_count, width, label=lbl, bottom=bottom)
    bottom += weight_count

ax.legend(bbox_to_anchor=(0.5, 1), loc="lower center", ncol=2)

fig.tight_layout(pad=1.5)

plt.savefig('baseline_traffic_a.pdf', bbox_inches='tight', pad_inches=.15, dpi=600)
# plt.show()
