Overview
====

This repository contains code and scripts that were used in preparing our manuscript entitled, "Novel signaling pathways underlying familial breast cancer susceptibility." Below we describe prerequisite software that must be installed and the various steps in the analysis process. We also provide various notes to help users understand our approach.

Prerequisite Software
====

  python (we used v2.6.6)

  scipy/numpy

  R

    gdata package

    e1071 package

  (Install the following tools within a "Software" directory.)

    FastQC

    samtools-0.1.18

    bamtools

    bwa-0.6.1

    GenomeAnalysisTK-1.5-3-gbb2c10b

    GenomeAnalysisTK-2.3-4-g57ea19f

    picard-tools-1.64

    snpEff_3_1

    dbNSFP2

Analysis Steps
====

The analysis can be executed in stages. The ```scripts/preprocess``` script contains commands for normalizing and summarizing the gene-expression data and for converting and filtering the data. The ```scripts/mlflex``` script provides commands for performing the machine-learning (classification analyses). This step will be very computationally intensive and can be executed across many cores and servers. The ```scripts/postprocess``` script contains code for summarizing the results of the machine-learning analysis and the gene-expression data in general.

The exome-sequencing data for the Utah and TCGA data sets were performed separately. These are provided in the scripts entitled, ```scripts/utahexome``` and ```scripts/tcga```, respectively.

Notes
====

Raw microarray files can be downloaded from GEO (GSE47682). Place them in the "raw" directory. They should be separated into subdirectories called utah, ontario1, and ontario2.

For the gene expression analyses, you may get slightly different results depending on version of scipy/numpy you use. (We used scipy version 0.8.0 and numpy version 1.5.1.) However, the downstream results should be similar.

We identified genes whose expresson was correlated with demographic / clinical variables and excluded those (described in manuscript). The data file containing these variables is not here. In addition, the exome-sequencing data require security approvals for access. Please contact the authors for access to these data.

Please secontact stephen_piccolo [at] byu [dot] edu with any questions.
