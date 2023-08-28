# Opera + DLRM Co-design Evaluation

Prerequisites:

* Python 3 (and as always, using a virtual environment is recommended)

```sh
pip install -r requirements.txt
```

You will also need the SLURM log files from the USC Discovery cluster jobs and the htsim log files produced by those jobs (e.g. drop or symlink in an `exp/Discovery/` directory.
Note that the htsim executions for Opera do not produce a separate log file, only the SLURM log.


## Scripts

* `traffic/est_ring_allreduce_traffic.py`: estimate traffic proportions from an htsim log file for a simulation of fat-tree using ring all-reduce; this is a *heuristic* that only work when the ring all-reduce actually uses all nodes, so results must be verified manually!


## Figures

* `tasks/plot_task_end_times-multi.py`: plot task end times for fat-tree and Opera executions; requires htsim and SLURM log files as input
* `times/plot_{baseline,bs1k,bs2k,fs40,fs93}_{a,i}.py`: plot simulated training iteration times; values captured from the end of htsim or SLURM log files.
* `traffic/plot_{baseline,bs1k,bs2k,fs40,fs93}_traffic_{a,i}.py`: plot traffic proportions; values produced using `est_ring_allreduce_traffic.py` -- in some cases, e.g., for Model-I at 1024 nodes, the estimate results are incorrect and must be adjusted manually since the ring exchange doesn't utilize all nodes.


## Notes

It seems that htsim log files either don't always include all FCT flows or are just not consistent with the "finished one task" lines in the SLURM log files.
If you try to plot start and end times FCT flows from the htsim log files, they sometimes do not seem to use the entire reported "FinalFinish" simulated runtime.
We did not see an easy way to accurately map tasks reported in the SLURM log file to FCT flows in the htsim log file (but that doesn't mean it's not possible).
