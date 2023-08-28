import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(6, 3.5)

ax.set_xlabel('Nodes', fontsize=16)
ax.set_ylabel('Traffic Proportion', fontsize=16)

node_counts = ['16', '128', '1024']
traffic = {}
# Scripted estimate for 1024 value of 0.4008872256641237 misses some all-reduce exchanges
traffic["All-reduce traffic"] = [0.0276194269682863, 0.07908444563655101, 0.4041381935374884]
traffic["Other traffic"] = [1 - t for t in traffic["All-reduce traffic"]]
width = 0.5

bottom = np.zeros(3)
for lbl, weight_count in traffic.items():
    p = ax.bar(node_counts, weight_count, width, label=lbl, bottom=bottom)
    bottom += weight_count

ax.legend(bbox_to_anchor=(0.5, 1), loc="lower center", ncol=2)

fig.tight_layout(pad=1.5)

plt.savefig('baseline_traffic_i.pdf', bbox_inches='tight', pad_inches=.15, dpi=600)
# plt.show()
