# Opera + DLRM Co-design Evaluation

Evaluation scripts for the paper:

Connor Imes, Andrew Rittenbach, Peng Xie, Dong In D. Kang, John Paul Walters, and Stephen P. Crago. 2024. Evaluating Deep Learning Recommendation Model Training Scalability with the Dynamic Opera Network. In Proceedings of the 4th Workshop on Machine Learning and Systems (EuroMLSys '24). Association for Computing Machinery, New York, NY, USA, 169–175. https://doi.org/10.1145/3642970.3655825

```BibTex
@inproceedings{OperaDLRM,
author = {Imes, Connor and Rittenbach, Andrew and Xie, Peng and Kang, Dong In D. and Walters, John Paul and Crago, Stephen P.},
title = {Evaluating Deep Learning Recommendation Model Training Scalability with the Dynamic Opera Network},
year = {2024},
isbn = {9798400705410},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3642970.3655825},
doi = {10.1145/3642970.3655825},
abstract = {Deep learning is commonly used to make personalized recommendations to users for a wide variety of activities. However, deep learning recommendation model (DLRM) training is increasingly dominated by all-to-all and many-to-many communication patterns. While there are a wide variety of algorithms to efficiently overlap communication and computation for many collective operations, these patterns are strictly limited by network bottlenecks. We propose co-designing DLRM model training with the recently proposed Opera network, which is designed to avoid multiple network hops using time-varying source-to-destination circuits. Using measurements from state-of-the-art NVIDIA A100 GPUs, we simulate DLRM model training on networks ranging from 16 to 1024 nodes and demonstrate up to 1.79\texttimes{} improvement using Opera compared with equivalent fat-tree networks. We identify important parameters affecting training time and demonstrate that careful co-design is needed to optimize training latency.},
booktitle = {Proceedings of the 4th Workshop on Machine Learning and Systems},
pages = {169–175},
numpages = {7},
keywords = {deep learning, dynamic networks, machine learning, networks, recommendation models},
location = {, Athens, Greece, },
series = {EuroMLSys '24}
}
```

For evaluation code and SLURM job scripts, see: https://github.com/usc-isi/STEAM-FlexFlow, branch `2024-euromlsys`.


## Prerequisites

* Python 3 (and as always, using a virtual environment is recommended)

```sh
pip install -r requirements.txt
```

You will also need the SLURM log files from the USC Discovery cluster jobs and the htsim log files produced by those jobs (e.g. drop or symlink in an `exp/Discovery/` directory).
Note that the htsim executions for Opera do not produce a separate log file, only the SLURM log.
Log files are hundreds of GB in total and thus too large to store in this git repository.


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
