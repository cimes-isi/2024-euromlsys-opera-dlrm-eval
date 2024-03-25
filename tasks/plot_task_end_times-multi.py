import sys
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

if len(sys.argv) < 4:
    print(f"Usage: {sys.argv[0]} ft_slurm_log_file opera_slurm_log_file output_pdf_file")
    sys.exit(1)
pdf_file = sys.argv[3]
assert 'slurm' not in pdf_file # idiot check to not overwrite our data


# ft_task_type_labels = ['Forward', 'Backward', 'Comm', 'Update', 'Barrier', 'Nominal Comm', 'AllReduce']
task_type_labels = ['Forward\nComp.', 'Backward\nComp.', 'Other\nComm.', 'AllReduce\nComm.']

ft_task_finish_time = []
ft_task_type = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        # 0x7ffd548b4670 finished one task, nfin 1 ntot 34358 type 0 now 33972400128
        if 'finished one task' in line:
            line = line.split(' ')
            ttype = min(int(line[9]), 3)
            ft_task_finish_time.append(float(line[-1]) / 1000000000)
            ft_task_type.append(ttype + 0.1)

opera_task_finish_time = []
opera_task_type = []
with open(sys.argv[2], 'r') as f:
    for line in f:
        # 0x7ffd548b4670 finished one task, nfin 1 ntot 34358 type 0 now 33972400128
        if 'finished one task' in line:
            line = line.split(' ')
            ttype = min(int(line[9]), 3)
            opera_task_finish_time.append(float(line[-1]) / 1000000000)
            opera_task_type.append(ttype - 0.1)

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(6, 2.75)

# rasterize to reduce the resulting file size (e.g., 8.4 MB -> 29 KB)
ax.scatter(ft_task_finish_time, ft_task_type, marker='2', c='#1f77b4', label='FatTree-Ring', rasterized=True)
ax.scatter(opera_task_finish_time, opera_task_type, marker='2', c='#d62728', label='Opera-DPS', rasterized=True)

ax.set_xlabel('Elapsed Training Time (ms)', fontsize=14)
ax.set_ylabel('Completed Tasks', fontsize=14)
ax.set_yticks([0, 1, 2, 3], labels=task_type_labels, fontsize=10)
# ax.legend(loc='lower right', fontsize=10, frameon=True, ncols=2)
ax.legend(bbox_to_anchor=(0.5, 1), loc="lower center", ncol=2)

fig.tight_layout(pad=1.5)

plt.savefig(pdf_file, bbox_inches='tight', pad_inches=.15, dpi=600)
# plt.show()
