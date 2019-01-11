# q2-metastorms
This is the official repository of Meta-Storms 2 for QIIME 2 plugin.

# Introduction
This is a QIIME 2 plugin of Meta-Storms 2. For details of Meta-Storms 2, see https://github.com/qibebt-bioinfo/meta-storms. For details on QIIME 2, see https://qiime2.org.

# Software Requirements
Please install the Meta-Storms 2 software first. For details of Meta-Storms 2 installation, see https://github.com/qibebt-bioinfo/meta-storms

# Installation guide
a. Download the package:
```
git clone https://github.com/qibebt-bioinfo/q2-metastorms.git
```
b. Install by installer:
```
cd q2-metastorms
pip install -e .
qiime dev refresh-cache
```

# Notics for input
The input OTUs should be parsed by QIIME 2 closed-reference clustering against the Greengenes 13_8 97% OTUs reference database. For details about the OTU clustering, see https://docs.qiime2.org/2018.11/tutorials/otu-clustering
