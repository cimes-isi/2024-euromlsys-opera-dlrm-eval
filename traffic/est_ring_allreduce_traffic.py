"""Estimate ring all-reduce vs non ring all-reduce traffic patterns."""
import sys
import numpy as np

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} htsim_log_file num_nodes")
    sys.exit(1)

nodes = int(sys.argv[2])
linecount = 0
xfer_sizes = np.zeros((nodes, nodes), dtype=np.float64)
xfer_sizes_unique = {}
xfer_sizes_unique_ar = {} # really just a heuristic, but probably accurate
xfer_counts = np.zeros((nodes, nodes), dtype=np.int64)
with open(sys.argv[1], 'r') as f:
    for line in f:
        if not line:
            break
        if 'FCT' in line:
            linecount += 1
            data = line.split(' ')
            # print(data)
            idx1 = int(data[1])
            idx2 = int(data[2])
            xfersize = int(data[3])
            print(idx1, idx2, xfersize)
            if xfersize in xfer_sizes_unique:
                xfer_sizes_unique[xfersize] += 1
                xfer_sizes_unique_ar[xfersize] = xfer_sizes_unique_ar[xfersize] and ((idx1 + 1) % nodes == idx2)
            else:
                xfer_sizes_unique[xfersize] = 1
                xfer_sizes_unique_ar[xfersize] = (idx1 + 1) % nodes == idx2
            xfer_sizes[idx1, idx2] += xfersize
            xfer_counts[idx1, idx2] += 1

print(f'Total transfer size: {xfer_sizes.sum()}')
print(f'Line count: {linecount}')

# Traffic along the [increasing] diagonal is mostly ring AR, but may include other traffic
xfer_size_sum = xfer_sizes.sum()
xfer_size_sum_diag = sum(xfer_sizes[n, (n + 1) % nodes] for n in range(nodes))
xfer_count_sum = xfer_counts.sum()
xfer_count_sum_diag = sum(xfer_counts[n, (n + 1) % nodes] for n in range(nodes))
print(f'Diagonal traffic portion by count: {xfer_count_sum_diag / xfer_count_sum}')
print(xfer_count_sum, xfer_count_sum_diag, xfer_count_sum_diag / xfer_count_sum)
print(f'Diagonal traffic portion by size:  {xfer_size_sum_diag / xfer_size_sum}')
print(xfer_size_sum, xfer_size_sum_diag, xfer_size_sum_diag / xfer_size_sum)

# Traffic that's ONLY along the [increasing] diagonal is a more accurate ring AR estimate
ar_count_sum = 0
ar_size_sum = 0
non_ar_count_sum = 0
non_ar_size_sum = 0
total_count = 0
total_sum = 0
print('xfersize: count: is_likely_allreduce')
for xfersize, count in xfer_sizes_unique.items():
    is_likely_allreduce = xfer_sizes_unique_ar[xfersize]
    print(f'{xfersize}: {count}: {is_likely_allreduce}')
    size = count * xfersize
    total_count += count
    total_sum += size
    if is_likely_allreduce:
        ar_count_sum += count
        ar_size_sum += size
    else:
        non_ar_count_sum += count
        non_ar_size_sum += size
# print(total_sum, ar_size_sum, non_ar_size_sum, ar_size_sum/total_sum)
print(f'Estimated all-reduce traffic portion by count: {ar_count_sum / total_count}')
print(f'Estimated all-reduce traffic portion by size:  {ar_size_sum / total_sum}')
