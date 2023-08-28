import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(6, 3.5)

ax.set_xlabel('Nodes', fontsize=16)
ax.set_ylabel('Traffic Proportion', fontsize=16)

node_counts = ['16', '128', '1024']
traffic = {}
# Scripted estimate for 1024 value of 0.14380984758894025 misses some all-reduce exchanges
traffic["All-reduce traffic"] = [0.007050913382492167, 0.02101774387638388, 0.1449800203950673]
traffic["Other traffic"] = [1 - t for t in traffic["All-reduce traffic"]]
width = 0.5

bottom = np.zeros(3)
for lbl, weight_count in traffic.items():
    p = ax.bar(node_counts, weight_count, width, label=lbl, bottom=bottom)
    bottom += weight_count

ax.legend(bbox_to_anchor=(0.5, 1), loc="lower center", ncol=2)

fig.tight_layout(pad=1.5)

plt.savefig('bs2k_traffic_i.pdf', bbox_inches='tight', pad_inches=.15, dpi=600)
# plt.show()
